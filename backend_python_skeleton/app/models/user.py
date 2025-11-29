from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

# ---------- Base Schema ----------
class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name of the user")
    email: EmailStr = Field(..., description="Unique email address of the user")
    skills: Optional[List[str]] = Field(default_factory=list, description="List of user's skills")


# ---------- Create Schema ----------
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="User password")
    

# ---------- Update Schema ----------
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    skills: Optional[List[str]] = None
    password: Optional[str] = Field(None, min_length=6)


# ---------- Output Schema (API Response) ----------
class UserOut(UserBase):
    id: int = Field(..., description="User ID")
    email_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True   # SQLAlchemy compatibility
        allow_population_by_field_name = True
