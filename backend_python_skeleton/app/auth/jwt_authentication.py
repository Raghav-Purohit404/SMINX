from datetime import datetime, timedelta
from jose import jwt, JWTError
import os

JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret-change-me")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXP_HOURS = int(os.getenv("JWT_EXP_HOURS", "24"))


def create_access_token(claims: dict) -> tuple[str, datetime]:
    """
    Create a JWT access token and return (token, expiry_time)
    """
    now = datetime.utcnow()
    expiry = now + timedelta(hours=JWT_EXP_HOURS)

    payload = claims.copy()
    payload.update({
        "iat": int(now.timestamp()),
        "exp": int(expiry.timestamp()),
    })

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token, expiry


def verify_access_token(token: str) -> dict:
    """
    Verify JWT token and return decoded payload
    """
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError:
        raise ValueError("Invalid or expired token")
