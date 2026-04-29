"""
Chat request/response schemas
"""
from typing import Optional, List
from pydantic import BaseModel, Field


class ChatMessageSchema(BaseModel):
    """Chat message schema"""

    role: str = Field(..., description="'user' or 'assistant'")
    content: str = Field(..., description="Message content")


class ChatRequestSchema(BaseModel):
    """Chat request schema"""

    session_id: str = Field(..., description="Chat session ID")
    message: str = Field(..., description="User message")
    topic: Optional[str] = Field(default="general", description="Topic: grammar, vocabulary, reading, listening")
    difficulty: Optional[str] = Field(default="A2", description="CEFR level: A2, B1, B2")
    language: Optional[str] = Field(default="en", description="Interface language: en, it")


class ChatResponseSchema(BaseModel):
    """Chat response schema"""

    session_id: str
    message_id: str
    response: str
    tokens_used: int
    thinking_process: Optional[str] = None


class ChatHistorySchema(BaseModel):
    """Chat history schema"""

    session_id: str
    messages: List[ChatMessageSchema]
    topic: str
    difficulty: str
    language: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True
