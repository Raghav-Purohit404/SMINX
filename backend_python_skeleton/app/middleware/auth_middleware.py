# app/middleware/auth_middleware.py
from fastapi import Depends, HTTPException, Header
from jose import jwt, JWTError
import os

JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret-change-me")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

async def verify_token(authorization: str = Header(None)):
    """
    Dependency that extracts and verifies a Bearer JWT token from Authorization header.
    Returns the decoded claims (dict) on success.
    Raises HTTPException(401) on failures.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Malformed Authorization header")

    token = authorization.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as exc:
        raise HTTPException(status_code=401, detail=f"Invalid token: {exc}")

    # Minimal validation: ensure sub exists
    if "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    # return token payload so route handlers can access user info
    return payload

