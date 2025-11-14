from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# ---------- Base Schema ----------
class ProjectBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, description="Project title")
    description: Optional[str] = Field(None, description="Detailed description of the project")
    skills_required: Optional[List[str]] = Field(default_factory=list, description="Skills needed for the project")


# ---------- Create Schema ----------
class ProjectCreate(ProjectBase):
    owner_id: int = Field(..., description="User ID of the project owner")


# ---------- Update Schema ----------
class ProjectUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = None
    skills_required: Optional[List[str]] = Field(default_factory=list)


# ---------- Response Schema ----------
class ProjectOut(ProjectBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
