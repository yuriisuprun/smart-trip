"""
Configuration settings for the application
"""
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "postgresql://italian_user:italian_pass@localhost:5432/italian_tutor"

    # Vector DB
    QDRANT_URL: str = "http://localhost:6333"
    QDRANT_API_KEY: str = ""

    # OpenAI
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4-turbo-preview"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"

    # Auth
    CLERK_SECRET_KEY: str = ""

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3335",
        "http://localhost:8000",
        "http://127.0.0.1:3335",
    ]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1", "0.0.0.0"]

    # Sentry
    SENTRY_DSN: str = ""

    # LLM Settings
    LLM_TEMPERATURE: float = 0.7
    LLM_MAX_TOKENS: int = 2000
    LLM_TOP_P: float = 0.9

    # Memory Settings
    SHORT_TERM_MEMORY_SIZE: int = 20
    LONG_TERM_MEMORY_ENABLED: bool = True

    # RAG Settings
    RAG_CHUNK_SIZE: int = 500
    RAG_CHUNK_OVERLAP: int = 50
    RAG_TOP_K: int = 5

    # Language Settings
    SUPPORTED_LANGUAGES: List[str] = ["en", "it"]
    DEFAULT_LANGUAGE: str = "en"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
