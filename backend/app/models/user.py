"""
User model
"""
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Float, Integer, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    """User model"""

    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)  # Clerk user ID
    email = Column(String, unique=True, index=True)
    name = Column(String)
    cefr_level = Column(String, default="A2")  # A2, B1, B2
    total_score = Column(Float, default=0.0)
    total_questions = Column(Integer, default=0)
    weak_areas = Column(JSON, default={})  # {"grammar": 0.5, "vocabulary": 0.6}
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    sessions = relationship("ChatSession", back_populates="user", cascade="all, delete-orphan")
    mistakes = relationship("Mistake", back_populates="user", cascade="all, delete-orphan")
    skill_progress = relationship("SkillProgress", back_populates="user", cascade="all, delete-orphan")
    quiz_attempts = relationship("QuizAttempt", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.email}>"
