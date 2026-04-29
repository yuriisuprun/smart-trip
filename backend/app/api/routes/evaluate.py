"""
Evaluation endpoints
"""
import logging
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import QuizAttempt, User
from app.schemas.evaluate import EvaluateRequestSchema, EvaluateResponseSchema
from app.services.llm import llm_service
from app.services.memory import MemoryService

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/")
async def evaluate_answer(
    request: EvaluateRequestSchema,
    db: Session = Depends(get_db),
):
    """Evaluate a student's answer"""
    try:
        # Evaluate using LLM with language support
        feedback = await llm_service.evaluate_answer(
            question=request.question,
            user_answer=request.user_answer,
            correct_answer=request.correct_answer,
            language=request.language or "en",
        )

        # Store attempt
        attempt_id = f"attempt_{uuid.uuid4()}"
        attempt = QuizAttempt(
            id=attempt_id,
            user_id=request.user_id,
            quiz_id="general",
            question_id=f"q_{uuid.uuid4()}",
            user_answer=request.user_answer,
            correct_answer=request.correct_answer or "",
            score=feedback.get("score", 0),
            feedback=feedback.get("explanation", ""),
        )
        db.add(attempt)

        # Update user progress
        user = db.query(User).filter(User.id == request.user_id).first()
        if user:
            user.total_questions += 1
            user.total_score = (
                (user.total_score * (user.total_questions - 1) + feedback.get("score", 0))
                / user.total_questions
            )

        # Update skill progress
        memory_service = MemoryService(db)
        memory_service.update_skill_progress(
            user_id=request.user_id,
            skill=request.topic,
            is_correct=feedback.get("is_correct", False),
            score=feedback.get("score", 0),
        )

        # Record mistakes if any
        if not feedback.get("is_correct", False):
            for error in feedback.get("grammar_errors", []):
                memory_service.record_mistake(
                    user_id=request.user_id,
                    topic=request.topic,
                    mistake_type=error.get("error", "unknown"),
                    user_answer=request.user_answer,
                    correct_answer=request.correct_answer or "",
                    explanation=error.get("explanation", ""),
                )

        memory_service.update_weak_areas(request.user_id)
        db.commit()

        return EvaluateResponseSchema(
            attempt_id=attempt_id,
            feedback=feedback,
            tokens_used=0,
        )

    except Exception as e:
        logger.error(f"Error evaluating answer: {e}")
        raise HTTPException(status_code=500, detail=str(e))
