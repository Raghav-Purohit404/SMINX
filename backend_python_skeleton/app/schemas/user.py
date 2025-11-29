from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

# ---------- Base Schema ----------
class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name of the user")
    email: EmailStr = Field(..., description="User's email address")
    skills: List[str] = Field(default_factory=list, description="List of user's skills")

# ---------- Create Schema ----------
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Password for authentication")

# ---------- Update Schema ----------
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50, description="Updated name")
    email: Optional[EmailStr] = Field(None, description="Updated email address")
    skills: Optional[List[str]] = Field(default_factory=list, description="Updated skills")
    password: Optional[str] = Field(None, min_length=6, description="Updated password")

# ---------- Response Schema ----------
class UserOut(UserBase):
    id: str
    email_verified: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

# ---------- OTP Schemas ----------
class UserSendOTP(BaseModel):
    email: EmailStr = Field(..., description="Email to send OTP to")

class UserVerifyOTP(BaseModel):
    email: EmailStr = Field(..., description="Email to verify")
    otp_code: str = Field(..., min_length=4, max_length=6, description="OTP code received by email")

