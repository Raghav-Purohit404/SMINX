from fastapi import HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt
import os

class LoginSchema(BaseModel):
    email: str

JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret-change-me")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXP_HOURS = int(os.getenv("JWT_EXP_HOURS", "24"))
COLLEGE_EMAIL_DOMAIN = os.getenv("COLLEGE_EMAIL_DOMAIN", "@college.edu")

async def login(payload: LoginSchema):
    email = payload.email.strip().lower()
    if not email.endswith(COLLEGE_EMAIL_DOMAIN):
        raise HTTPException(status_code=400, detail=f"Use college email ending with {COLLEGE_EMAIL_DOMAIN}")

    now = datetime.utcnow()
    expiry = now + timedelta(hours=JWT_EXP_HOURS)
    claims = {
        "sub": email,
        "iat": int(now.timestamp()),
        "exp": int(expiry.timestamp()),
        "user_id": f"user:{email}",
        "email": email,
    }
    token = jwt.encode(claims, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"token": token, "token_type": "bearer", "expires_at": expiry.isoformat(), "email": email}

