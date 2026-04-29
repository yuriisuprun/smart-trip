"""
User service for managing user creation and synchronization with Clerk
"""
import logging
from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.database import get_db

logger = logging.getLogger(__name__)


class UserService:
    """Service for user management"""
    
    @staticmethod
    def get_or_create_user(
        db: Session,
        user_id: str,
        email: Optional[str] = None,
        name: Optional[str] = None
    ) -> User:
        """
        Get existing user or create new one from Clerk data
        """
        # Try to get existing user
        user = db.query(User).filter(User.id == user_id).first()
        
        if user:
            # Update user info if provided and different
            updated = False
            if email and user.email != email:
                user.email = email
                updated = True
            if name and user.name != name:
                user.name = name
                updated = True
            
            if updated:
                db.commit()
                db.refresh(user)
                logger.info(f"Updated user {user_id}")
            
            return user
        
        # Create new user
        user = User(
            id=user_id,
            email=email or f"user_{user_id}@example.com",  # Fallback email
            name=name or "User",  # Fallback name
            cefr_level="A2",  # Default level
            total_score=0.0,
            total_questions=0,
            weak_areas={}
        )
        
        db.add(user)
        db.commit()
        db.refresh(user)
        
        logger.info(f"Created new user {user_id}")
        return user
    
    @staticmethod
    def update_user_progress(
        db: Session,
        user_id: str,
        score_delta: float,
        questions_delta: int = 1
    ) -> User:
        """
        Update user's overall progress
        """
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError(f"User {user_id} not found")
        
        user.total_score += score_delta
        user.total_questions += questions_delta
        
        db.commit()
        db.refresh(user)
        
        return user
    
    @staticmethod
    def update_weak_areas(
        db: Session,
        user_id: str,
        topic: str,
        accuracy: float
    ) -> User:
        """
        Update user's weak areas based on performance
        """
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError(f"User {user_id} not found")
        
        if not user.weak_areas:
            user.weak_areas = {}
        
        # Update weak area score (lower is worse)
        current_score = user.weak_areas.get(topic, 1.0)
        # Weighted average with more weight on recent performance
        new_score = (current_score * 0.7) + (accuracy * 0.3)
        user.weak_areas[topic] = round(new_score, 2)
        
        db.commit()
        db.refresh(user)
        
        return user


# Global service instance
user_service = UserService()