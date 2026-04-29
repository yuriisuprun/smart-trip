"""
Evaluation request/response schemas
"""
from typing import Optional, List
from pydantic import BaseModel, Field


class EvaluateRequestSchema(BaseModel):
    """Evaluation request schema"""

    question: str = Field(..., description="The question asked")
    user_answer: str = Field(..., description="Student's answer")
    correct_answer: Optional[str] = Field(None, description="Correct answer (for multiple choice)")
    question_type: str = Field(default="open", description="'open' or 'multiple_choice'")
    topic: str = Field(default="general", description="Topic: grammar, vocabulary, reading, listening, writing")
    language: Optional[str] = Field(default="en", description="Interface language: en, it")


class EvaluationFeedbackSchema(BaseModel):
    """Evaluation feedback schema"""

    score: float = Field(..., description="Score 0-10")
    is_correct: bool
    corrections: List[str] = Field(default_factory=list)
    explanation: str
    improvement_suggestions: List[str] = Field(default_factory=list)
    grammar_errors: List[dict] = Field(default_factory=list)


class EvaluateResponseSchema(BaseModel):
    """Evaluation response schema"""

    attempt_id: str
    feedback: EvaluationFeedbackSchema
    tokens_used: int
