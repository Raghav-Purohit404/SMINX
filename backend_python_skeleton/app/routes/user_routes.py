from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserOut, UserSendOTP, UserVerifyOTP
from app.services.user_services import create_user, send_otp, verify_otp, get_user
from app.database import get_db
from app.core.security import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)

@router.post("/send-otp")
async def request_otp(payload: UserSendOTP, db: AsyncSession = Depends(get_db)):
    try:
        otp = await send_otp(db, payload.email)
        return {"message": "OTP sent", "otp": otp}  # remove otp in prod
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.post("/verify-otp")
async def confirm_otp(payload: UserVerifyOTP, db: AsyncSession = Depends(get_db)):
    try:
        await verify_otp(db, payload.email, payload.otp_code)
        return {"message": "Email verified successfully"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

