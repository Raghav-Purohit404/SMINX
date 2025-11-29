from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from app.models.user_model import User
from app.schemas.user import UserCreate, UserUpdate
from datetime import datetime, timedelta
import random

OTP_EXPIRY_MINUTES = 10

# ------------------- Create User -------------------
async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    new_user = User(
        name=user_in.name,
        email=user_in.email,
        hashed_password=user_in.password
    )
    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user)
        return new_user
    except IntegrityError:
        await db.rollback()
        raise ValueError("User with this email already exists")

# ------------------- Get User By ID -------------------
async def get_user(db: AsyncSession, user_id: str):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

# ------------------- Update User -------------------
async def update_user(db: AsyncSession, user_id: str, user_in: UserUpdate):
    user = await get_user(db, user_id)
    if not user:
        return None
    for k, v in user_in.dict(exclude_unset=True).items():
        setattr(user, k, v)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

# ------------------- Delete User -------------------
async def delete_user(db: AsyncSession, user_id: str):
    user = await get_user(db, user_id)
    if not user:
        return False
    await db.delete(user)
    await db.commit()
    return True

# ------------------- OTP Functions -------------------
async def send_otp(db: AsyncSession, email: str) -> str:
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        raise ValueError("User not found")
    otp = str(random.randint(1000, 9999))
    user.otp_code = otp
    user.otp_expiry = datetime.utcnow() + timedelta(minutes=OTP_EXPIRY_MINUTES)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return otp

async def verify_otp(db: AsyncSession, email: str, otp_code: str):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        raise ValueError("User not found")
    if not user.otp_code or datetime.utcnow() > user.otp_expiry:
        raise ValueError("OTP expired or not requested")
    if user.otp_code != otp_code:
        raise ValueError("Invalid OTP")
    user.email_verified = True
    user.otp_code = None
    user.otp_expiry = None
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return True

