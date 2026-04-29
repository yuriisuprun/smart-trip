"""
Memory management service for short-term and long-term learning
"""
import logging
from typing import List, Dict, Optional
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.models import ChatMessage, Mistake, SkillProgress, User
from app.core.config import settings

logger = logging.getLogger(__name__)


class MemoryService:
    """Memory service for managing learning context"""

    def __init__(self, db: Session):
        """Initialize memory service"""
        self.db = db
        self.short_term_size = settings.SHORT_TERM_MEMORY_SIZE

    def get_short_term_memory(self, session_id: str) -> List[Dict]:
        """Get recent messages from current session"""
        messages = (
            self.db.query(ChatMessage)
            .filter(ChatMessage.session_id == session_id)
            .order_by(ChatMessage.created_at.desc())
            .limit(self.short_term_size)
            .all()
        )

        return [
            {
                "role": msg.role,
                "content": msg.content,
                "timestamp": msg.created_at.isoformat(),
            }
            for msg in reversed(messages)
        ]

    def get_long_term_memory(self, user_id: str) -> Dict:
        """Get user's long-term learning profile"""
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return {}

        # Get recent mistakes (last 30 days)
        recent_mistakes = (
            self.db.query(Mistake)
            .filter(
                Mistake.user_id == user_id,
                Mistake.created_at >= datetime.now(timezone.utc) - timedelta(days=30),
            )
            .order_by(Mistake.frequency.desc())
            .limit(10)
            .all()
        )

        # Get skill progress
        skill_progress = (
            self.db.query(SkillProgress)
            .filter(SkillProgress.user_id == user_id)
            .all()
        )

        return {
            "cefr_level": user.cefr_level,
            "weak_areas": user.weak_areas or {},
            "total_score": user.total_score,
            "total_questions": user.total_questions,
            "recent_mistakes": [
                {
                    "topic": m.topic,
                    "mistake_type": m.mistake_type,
                    "frequency": m.frequency,
                    "explanation": m.explanation,
                }
                for m in recent_mistakes
            ],
            "skill_progress": [
                {
                    "skill": sp.skill,
                    "level": sp.level,
                    "score": sp.score,
                    "accuracy": sp.correct_answers / sp.attempts if sp.attempts > 0 else 0,
                }
                for sp in skill_progress
            ],
        }

    def record_mistake(
        self,
        user_id: str,
        topic: str,
        mistake_type: str,
        user_answer: str,
        correct_answer: str,
        explanation: str,
    ) -> Mistake:
        """Record a mistake for learning"""
        # Check if similar mistake exists
        existing = (
            self.db.query(Mistake)
            .filter(
                Mistake.user_id == user_id,
                Mistake.topic == topic,
                Mistake.mistake_type == mistake_type,
            )
            .first()
        )

        if existing:
            existing.frequency += 1
            existing.updated_at = datetime.now(timezone.utc)
            self.db.commit()
            return existing

        mistake = Mistake(
            id=f"mistake_{user_id}_{datetime.now(timezone.utc).timestamp()}",
            user_id=user_id,
            topic=topic,
            mistake_type=mistake_type,
            user_answer=user_answer,
            correct_answer=correct_answer,
            explanation=explanation,
        )
        self.db.add(mistake)
        self.db.commit()
        return mistake

    def update_skill_progress(
        self,
        user_id: str,
        skill: str,
        is_correct: bool,
        score: float,
    ) -> SkillProgress:
        """Update skill progress"""
        progress = (
            self.db.query(SkillProgress)
            .filter(
                SkillProgress.user_id == user_id,
                SkillProgress.skill == skill,
            )
            .first()
        )

        if not progress:
            progress = SkillProgress(
                id=f"skill_{user_id}_{skill}_{datetime.now(timezone.utc).timestamp()}",
                user_id=user_id,
                skill=skill,
            )
            self.db.add(progress)

        progress.attempts += 1
        if is_correct:
            progress.correct_answers += 1

        # Update score (weighted average)
        progress.score = (progress.score * (progress.attempts - 1) + score) / progress.attempts
        progress.last_practiced = datetime.now(timezone.utc)

        # Update CEFR level based on score
        if progress.score >= 80:
            progress.level = "B1"
        elif progress.score >= 60:
            progress.level = "A2"
        else:
            progress.level = "A1"

        self.db.commit()
        return progress

    def update_weak_areas(self, user_id: str):
        """Update user's weak areas based on skill progress"""
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return

        skill_progress = (
            self.db.query(SkillProgress)
            .filter(SkillProgress.user_id == user_id)
            .all()
        )

        weak_areas = {}
        for sp in skill_progress:
            accuracy = sp.correct_answers / sp.attempts if sp.attempts > 0 else 0
            if accuracy < 0.7:  # Less than 70% accuracy
                weak_areas[sp.skill] = accuracy

        user.weak_areas = weak_areas
        self.db.commit()
