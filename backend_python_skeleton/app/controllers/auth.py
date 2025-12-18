from fastapi import HTTPException
from pydantic import BaseModel
import os

from app.auth.jwt_authentication import create_access_token


# --------------------------------------------------
# CONFIG
# --------------------------------------------------
COLLEGE_EMAIL_DOMAIN = os.getenv("COLLEGE_EMAIL_DOMAIN", "@college.edu")


# --------------------------------------------------
# REQUEST SCHEMA
# --------------------------------------------------
class LoginSchema(BaseModel):
    email: str


# --------------------------------------------------
# LOGIN CONTROLLER
# --------------------------------------------------
async def login(payload: LoginSchema):
    """
    Validate login request and issue a JWT token.
    """

    email = payload.email.strip().lower()

    # Enforce college email restriction
    if not email.endswith(COLLEGE_EMAIL_DOMAIN):
        raise HTTPException(
            status_code=400,
            detail=f"Use college email ending with {COLLEGE_EMAIL_DOMAIN}"
        )

    # JWT claims
    claims = {
        "sub": email,
        "email": email,
        "user_id": f"user:{email}",
        "role": "student"
    }

    # Create JWT using shared authentication module
    token, expiry = create_access_token(claims)

    return {
        "token": token,
        "token_type": "bearer",
        "expires_at": expiry.isoformat(),
        "email": email
    }
