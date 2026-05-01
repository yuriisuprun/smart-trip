"""
RAG (Retrieval-Augmented Generation) service
"""
import logging
from typing import List, Optional
from app.core.config import settings

logger = logging.getLogger(__name__)

# Check if we have a valid OpenAI API key
def has_valid_openai_key():
    """Check if OpenAI API key is properly configured"""
    api_key = settings.OPENAI_API_KEY
    return api_key and api_key != "sk-your-openai-api-key-here" and len(api_key) > 20

# Import appropriate service based on API key availability
if has_valid_openai_key():
    try:
        from qdrant_client import QdrantClient
        from qdrant_client.models import Distance, VectorParams, PointStruct
        from langchain_openai import OpenAIEmbeddings
        
        class RAGService:
            """RAG service for retrieving relevant context"""

            def __init__(self):
                """Initialize RAG service"""
                self.client = QdrantClient(url=settings.QDRANT_URL)
                self.embeddings = OpenAIEmbeddings(
                    model=settings.OPENAI_EMBEDDING_MODEL,
                    api_key=settings.OPENAI_API_KEY,
                )
                self.collection_name = "italian_tutor"
                self._ensure_collection()

            def _ensure_collection(self):
                """Ensure collection exists"""
                try:
                    self.client.get_collection(self.collection_name)
                except Exception:
                    logger.info(f"Creating collection {self.collection_name}")
                    self.client.create_collection(
                        collection_name=self.collection_name,
                        vectors_config=VectorParams(
                            size=1536,  # text-embedding-3-small dimension
                            distance=Distance.COSINE,
                        ),
                    )

            def add_document(
                self,
                doc_id: str,
                content: str,
                metadata: dict,
                chunk_size: int = 500,
            ):
                """Add document to vector DB with chunking"""
                try:
                    # Split content into chunks
                    chunks = self._chunk_text(content, chunk_size)

                    points = []
                    for i, chunk in enumerate(chunks):
                        chunk_id = f"{doc_id}_chunk_{i}"
                        embedding = self.embeddings.embed_query(chunk)

                        point = PointStruct(
                            id=hash(chunk_id) % (2**31),  # Convert to positive int
                            vector=embedding,
                            payload={
                                "doc_id": doc_id,
                                "chunk_index": i,
                                "content": chunk,
                                **metadata,
                            },
                        )
                        points.append(point)

                    if points:
                        self.client.upsert(
                            collection_name=self.collection_name,
                            points=points,
                        )
                        logger.info(f"Added {len(points)} chunks for document {doc_id}")
                except Exception as e:
                    logger.error(f"Error adding document: {e}")
                    raise

            def retrieve(
                self,
                query: str,
                top_k: int = 5,
                filters: Optional[dict] = None,
                cefr_level: Optional[str] = None,
                content_type: Optional[str] = None,
                topic: Optional[str] = None,
            ) -> List[dict]:
                """Retrieve relevant documents with enhanced filtering"""
                try:
                    query_embedding = self.embeddings.embed_query(query)

                    # Build filter conditions
                    filter_conditions = []
                    
                    if cefr_level:
                        filter_conditions.append({
                            "key": "cefr_level",
                            "match": {"value": cefr_level}
                        })
                    
                    if content_type:
                        filter_conditions.append({
                            "key": "content_type", 
                            "match": {"value": content_type}
                        })
                        
                    if topic:
                        filter_conditions.append({
                            "key": "subtopic",
                            "match": {"value": topic}
                        })
                    
                    # Add custom filters if provided
                    if filters:
                        for key, value in filters.items():
                            filter_conditions.append({
                                "key": key,
                                "match": {"value": value}
                            })

                    # Prepare search parameters
                    search_params = {
                        "collection_name": self.collection_name,
                        "query_vector": query_embedding,
                        "limit": top_k,
                    }
                    
                    # Add filter if conditions exist
                    if filter_conditions:
                        if len(filter_conditions) == 1:
                            search_params["query_filter"] = filter_conditions[0]
                        else:
                            search_params["query_filter"] = {
                                "must": filter_conditions
                            }

                    results = self.client.search(**search_params)

                    retrieved = []
                    for result in results:
                        retrieved.append({
                            "content": result.payload.get("content", ""),
                            "doc_id": result.payload.get("doc_id", ""),
                            "metadata": {
                                k: v for k, v in result.payload.items()
                                if k not in ["content", "doc_id", "chunk_index"]
                            },
                            "score": result.score,
                        })

                    return retrieved
                except Exception as e:
                    logger.error(f"Error retrieving documents: {e}")
                    return []

            def retrieve_by_cefr_level(
                self,
                query: str,
                cefr_level: str,
                top_k: int = 5,
            ) -> List[dict]:
                """Retrieve documents filtered by CEFR level"""
                return self.retrieve(
                    query=query,
                    top_k=top_k,
                    cefr_level=cefr_level
                )
            
            def retrieve_grammar_content(
                self,
                query: str,
                cefr_level: Optional[str] = None,
                topic: Optional[str] = None,
                top_k: int = 5,
            ) -> List[dict]:
                """Retrieve grammar-specific content"""
                return self.retrieve(
                    query=query,
                    top_k=top_k,
                    cefr_level=cefr_level,
                    content_type="grammar_rule",
                    topic=topic
                )
            
            def retrieve_exercises(
                self,
                query: str,
                cefr_level: Optional[str] = None,
                exercise_type: Optional[str] = None,
                top_k: int = 3,
            ) -> List[dict]:
                """Retrieve exercise content"""
                filters = {}
                if exercise_type:
                    filters["exercise_type"] = exercise_type
                    
                return self.retrieve(
                    query=query,
                    top_k=top_k,
                    cefr_level=cefr_level,
                    content_type="exercise",
                    filters=filters
                )
            
            def get_content_by_difficulty(
                self,
                query: str,
                min_difficulty: int,
                max_difficulty: int = 10,
                top_k: int = 5,
            ) -> List[dict]:
                """Retrieve content filtered by difficulty range"""
                # Note: This would require a range filter in Qdrant
                # For now, we'll retrieve and filter in Python
                results = self.retrieve(query=query, top_k=top_k * 2)
                
                filtered_results = []
                for result in results:
                    difficulty = result["metadata"].get("difficulty", 5)
                    if min_difficulty <= difficulty <= max_difficulty:
                        filtered_results.append(result)
                        if len(filtered_results) >= top_k:
                            break
                
                return filtered_results
            
            def _chunk_text(self, text: str, chunk_size: int = 500) -> List[str]:
                """Split text into chunks"""
                chunks = []
                words = text.split()

                current_chunk = []
                current_size = 0

                for word in words:
                    current_chunk.append(word)
                    current_size += len(word) + 1

                    if current_size >= chunk_size:
                        chunks.append(" ".join(current_chunk))
                        current_chunk = []
                        current_size = 0

                if current_chunk:
                    chunks.append(" ".join(current_chunk))

                return chunks

        # Global RAG service instance
        rag_service = RAGService()
        logger.info("✅ Using full RAG service with OpenAI embeddings")
        
    except Exception as e:
        logger.warning(f"Failed to initialize full RAG service: {e}")
        logger.info("🔄 Falling back to mock RAG service")
        from app.services.mock_rag import mock_rag_service
        rag_service = mock_rag_service
else:
    logger.warning("⚠️ OpenAI API key not configured or invalid")
    logger.info("🔄 Using mock RAG service for testing")
    from app.services.mock_rag import mock_rag_service
    rag_service = mock_rag_service
