"""
Learning progress and mistake tracking models
"""
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Float, Integer, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base


class Mistake(Base):
    """Mistake tracking model"""

    __tablename__ = "mistakes"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), index=True)
    topic = Column(String)  # "grammar", "vocabulary", etc.
    mistake_type = Column(String)  # "tense", "gender", "preposition", etc.
    user_answer = Column(Text)
    correct_answer = Column(Text)
    explanation = Column(Text)
    frequency = Column(Integer, default=1)  # How many times this mistake occurred
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    user = relationship("User", back_populates="mistakes")

    def __repr__(self):
        return f"<Mistake {self.id}>"


class SkillProgress(Base):
    """Skill progress tracking model"""

    __tablename__ = "skill_progress"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), index=True)
    skill = Column(String, index=True)  # "grammar", "vocabulary", "reading", "listening", "writing"
    level = Column(String, default="A2")  # CEFR level
    score = Column(Float, default=0.0)  # 0-100
    attempts = Column(Integer, default=0)
    correct_answers = Column(Integer, default=0)
    last_practiced = Column(DateTime)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    user = relationship("User", back_populates="skill_progress")

    def __repr__(self):
        return f"<SkillProgress {self.skill}>"


class QuizAttempt(Base):
    """Quiz attempt model"""

    __tablename__ = "quiz_attempts"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), index=True)
    quiz_id = Column(String, index=True)
    question_id = Column(String, index=True)
    user_answer = Column(Text)
    correct_answer = Column(Text)
    score = Column(Float)  # 0-10
    feedback = Column(Text)
    time_spent = Column(Integer)  # seconds
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    user = relationship("User", back_populates="quiz_attempts")

    def __repr__(self):
        return f"<QuizAttempt {self.id}>"
