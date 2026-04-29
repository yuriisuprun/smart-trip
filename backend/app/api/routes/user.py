"""
User profile endpoints
"""
import logging
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.auth import get_current_user, get_current_user_id
from app.models.user import User
from app.services.user import user_service

logger = logging.getLogger(__name__)
router = APIRouter()


class UserProfileSchema(BaseModel):
    """User profile schema"""
    id: str
    email: str
    name: str
    cefr_level: str
    total_score: float
    total_questions: int
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True


class UpdateProfileSchema(BaseModel):
    """Update profile schema"""
    name: Optional[str] = Field(None, description="User's display name")
    cefr_level: Optional[str] = Field(None, description="CEFR level: A1, A2, B1, B2")


@router.get("/profile", response_model=UserProfileSchema)
async def get_user_profile(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Get current user's profile"""
    try:
        # Ensure user exists in database and sync with Clerk data
        user = user_service.get_or_create_user(
            db=db,
            user_id=current_user["user_id"],
            email=current_user.get("email"),
            name=current_user.get("name")
        )

        return UserProfileSchema(
            id=user.id,
            email=user.email,
            name=user.name,
            cefr_level=user.cefr_level,
            total_score=user.total_score,
            total_questions=user.total_questions,
            created_at=user.created_at.isoformat(),
            updated_at=user.updated_at.isoformat(),
        )

    except Exception as e:
        logger.error(f"Error getting user profile: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/profile", response_model=UserProfileSchema)
async def update_user_profile(
    profile_update: UpdateProfileSchema,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user_id),
):
    """Update current user's profile"""
    try:
        user = db.query(User).filter(User.id == current_user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Update fields if provided
        if profile_update.name is not None:
            user.name = profile_update.name
        
        if profile_update.cefr_level is not None:
            if profile_update.cefr_level not in ["A1", "A2", "B1", "B2"]:
                raise HTTPException(status_code=400, detail="Invalid CEFR level")
            user.cefr_level = profile_update.cefr_level

        db.commit()
        db.refresh(user)

        return UserProfileSchema(
            id=user.id,
            email=user.email,
            name=user.name,
            cefr_level=user.cefr_level,
            total_score=user.total_score,
            total_questions=user.total_questions,
            created_at=user.created_at.isoformat(),
            updated_at=user.updated_at.isoformat(),
        )

    except Exception as e:
        logger.error(f"Error updating user profile: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/profile")
async def delete_user_account(
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user_id),
):
    """Delete current user's account and all associated data"""
    try:
        user = db.query(User).filter(User.id == current_user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Delete user (cascade will handle related data)
        db.delete(user)
        db.commit()

        return {"message": "Account deleted successfully"}

    except Exception as e:
        logger.error(f"Error deleting user account: {e}")
        raise HTTPException(status_code=500, detail=str(e))