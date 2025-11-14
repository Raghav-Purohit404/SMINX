# app/middleware/role_middleware.py
from fastapi import Depends, HTTPException
from app.core.database import get_db
from app.models.user import User
from sqlalchemy.orm import Session

def require_admin(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user or not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")
    return user
