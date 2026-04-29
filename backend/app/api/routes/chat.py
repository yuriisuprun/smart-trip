"""
Chat endpoints
"""
import logging
import uuid
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.auth import get_current_user_id
from app.models import ChatSession, ChatMessage, User
from app.schemas.chat import ChatRequestSchema, ChatHistorySchema
from app.services.rag import rag_service
from app.services.llm import llm_service
from app.services.memory import MemoryService
from app.services.user import user_service

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/")
async def chat(
    request: ChatRequestSchema,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user_id),
):
    """Chat endpoint with streaming response"""
    try:
        # Ensure user exists in database
        user_service.get_or_create_user(db, current_user_id)
        
        # Get or create session
        session = db.query(ChatSession).filter(
            ChatSession.id == request.session_id,
            ChatSession.user_id == current_user_id  # Ensure user owns session
        ).first()

        if not session:
            session = ChatSession(
                id=request.session_id,
                user_id=current_user_id,  # Use authenticated user ID
                topic=request.topic,
                difficulty=request.difficulty,
                language=request.language or "en",
            )
            db.add(session)
            db.commit()

        # Store user message
        user_msg_id = f"msg_{uuid.uuid4()}"
        user_msg = ChatMessage(
            id=user_msg_id,
            session_id=request.session_id,
            role="user",
            content=request.message,
        )
        db.add(user_msg)
        db.commit()

        # Get memory context
        memory_service = MemoryService(db)
        short_term = memory_service.get_short_term_memory(request.session_id)
        long_term = memory_service.get_long_term_memory(current_user_id)  # Use authenticated user ID

        # Retrieve relevant context from RAG with enhanced filtering
        user = db.query(User).filter(User.id == current_user_id).first()
        user_cefr_level = user.cefr_level if user else "A2"
        
        # Get grammar-specific content based on user's level and topic
        retrieved = rag_service.retrieve_grammar_content(
            query=request.message,
            cefr_level=user_cefr_level,
            topic=request.topic if request.topic != "general" else None,
            top_k=5,
        )
        
        # If no grammar content found, try general retrieval
        if not retrieved:
            retrieved = rag_service.retrieve(
                query=request.message,
                top_k=5,
                cefr_level=user_cefr_level
            )

        # Generate response using language-aware LLM service
        async def generate():
            response_text = ""
            
            # Use the updated LLM service with language support
            full_response = await llm_service.generate_tutoring_response(
                user_message=request.message,
                topic=request.topic,
                difficulty=request.difficulty,
                short_term_memory=short_term,
                long_term_memory=long_term,
                retrieved_context=retrieved,
                language=request.language or "en"
            )
            
            # Stream the response word by word for better UX
            words = full_response.split()
            for i, word in enumerate(words):
                chunk = word + (" " if i < len(words) - 1 else "")
                response_text += chunk
                yield chunk

            # Store assistant message
            assistant_msg = ChatMessage(
                id=f"msg_{uuid.uuid4()}",
                session_id=request.session_id,
                role="assistant",
                content=response_text,
            )
            db.add(assistant_msg)
            db.commit()

        return StreamingResponse(generate(), media_type="text/event-stream")

    except Exception as e:
        logger.error(f"Error in chat: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{session_id}")
async def get_chat_history(
    session_id: str,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user_id),
):
    """Get chat history for a session"""
    try:
        session = db.query(ChatSession).filter(
            ChatSession.id == session_id,
            ChatSession.user_id == current_user_id  # Ensure user owns session
        ).first()

        if not session:
            raise HTTPException(status_code=404, detail="Session not found")

        messages = db.query(ChatMessage).filter(
            ChatMessage.session_id == session_id
        ).order_by(ChatMessage.created_at).all()

        return ChatHistorySchema(
            session_id=session.id,
            messages=[
                {"role": msg.role, "content": msg.content}
                for msg in messages
            ],
            topic=session.topic,
            difficulty=session.difficulty,
            language=getattr(session, 'language', 'en'),
            created_at=session.created_at.isoformat(),
            updated_at=session.updated_at.isoformat(),
        )

    except Exception as e:
        logger.error(f"Error getting chat history: {e}")
        raise HTTPException(status_code=500, detail=str(e))
