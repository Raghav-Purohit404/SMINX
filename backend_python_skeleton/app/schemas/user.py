from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime


# ---------- Base Schema ----------
class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name of the user")
    email: EmailStr = Field(..., description="User's email address")
    skills: Optional[List[str]] = Field(default_factory=list, description="List of user's skills")


# ---------- Create Schema ----------
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Password for authentication")


# ---------- Update Schema ----------
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    skills: Optional[List[str]] = Field(default_factory=list)
    password: Optional[str] = Field(None, min_length=6)


# ---------- Response Schema ----------
class UserOut(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
