from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers import auth as auth_ctrl
from app.controllers.auth import LoginSchema
from app.models.user import UserCreate, UserOut
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

# ---------- Login Endpoint ----------
@router.post("/login", summary="Login with college email")
async def login(payload: LoginSchema):
    """
    Login using a college email; returns JWT token on success.
    """
    try:
        return await auth_ctrl.login(payload)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# ---------- Register Endpoint ----------
@router.post("/register", response_model=UserOut, summary="Register a new user")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Register a new user with hashed password.
    """
    return await auth_ctrl.register_user(db, user)

