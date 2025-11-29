# app/controllers/users.py
from typing import List
from app.models.user import UserCreate, UserOut
from fastapi import HTTPException
from datetime import datetime

# NOTE:
# Your repo doesn't include a SQLAlchemy user model file to persist users.
# Until you add a DB model, this controller returns a minimal UserOut object.
# Replace with DB insert + password hashing when you add a User model.

async def create_user(payload: UserCreate) -> UserOut:
    """
    Minimal create_user stub:
    - validates payload (Pydantic does that already)
    - returns a UserOut with fake id and timestamps so frontend can proceed.
    Replace with actual DB persistence and password hashing.
    """
    # simple sanity check
    email = payload.email.strip().lower()
    if not email:
        raise HTTPException(status_code=400, detail="Email required")

    now = datetime.utcnow()
    # create response object (no persistence yet)
    out = UserOut(
        id=1,  # placeholder id — update once you persist
        name=payload.name,
        email=email,
        skills=payload.skills or [],
        created_at=now,
        updated_at=now,
    )
    return out

