"""
Clerk authentication middleware and utilities
"""
import logging
from typing import Optional
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
import httpx
from app.core.config import settings

logger = logging.getLogger(__name__)

# Security scheme for Bearer token
security = HTTPBearer()


class ClerkAuth:
    """Clerk authentication handler"""
    
    def __init__(self):
        self.jwks_cache = {}
        self.jwks_url = "https://api.clerk.dev/v1/jwks"
    
    async def get_jwks(self) -> dict:
        """Get JWKS from Clerk"""
        if not self.jwks_cache:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.jwks_url)
                response.raise_for_status()
                self.jwks_cache = response.json()
        return self.jwks_cache
    
    async def verify_token(self, token: str) -> dict:
        """Verify Clerk JWT token"""
        try:
            # Decode token header to get kid
            unverified_header = jwt.get_unverified_header(token)
            kid = unverified_header.get("kid")
            
            if not kid:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token: missing kid"
                )
            
            # Get JWKS and find matching key
            jwks = await self.get_jwks()
            key = None
            for jwk in jwks.get("keys", []):
                if jwk.get("kid") == kid:
                    key = jwk
                    break
            
            if not key:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token: key not found"
                )
            
            # Verify token
            payload = jwt.decode(
                token,
                key,
                algorithms=["RS256"],
                audience=settings.CLERK_SECRET_KEY,
                options={"verify_aud": False}  # Clerk uses different audience format
            )
            
            return payload
            
        except JWTError as e:
            logger.error(f"JWT verification failed: {e}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )


# Global auth instance
clerk_auth = ClerkAuth()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    """
    Dependency to get current authenticated user from Clerk token
    Returns user payload with user_id (sub field)
    """
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header required"
        )
    
    token = credentials.credentials
    payload = await clerk_auth.verify_token(token)
    
    # Extract user ID from Clerk token (sub field)
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token: missing user ID"
        )
    
    return {
        "user_id": user_id,
        "email": payload.get("email"),
        "name": payload.get("name"),
        "payload": payload
    }


async def get_current_user_id(
    current_user: dict = Depends(get_current_user)
) -> str:
    """
    Dependency to get just the user ID from authenticated user
    """
    return current_user["user_id"]


# Optional auth dependency for endpoints that can work with or without auth
async def get_optional_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer(auto_error=False))
) -> Optional[dict]:
    """
    Optional authentication dependency
    Returns user info if token is provided and valid, None otherwise
    """
    if not credentials:
        return None
    
    try:
        token = credentials.credentials
        payload = await clerk_auth.verify_token(token)
        user_id = payload.get("sub")
        
        if user_id:
            return {
                "user_id": user_id,
                "email": payload.get("email"),
                "name": payload.get("name"),
                "payload": payload
            }
    except HTTPException:
        # Invalid token, but this is optional auth
        pass
    
    return None