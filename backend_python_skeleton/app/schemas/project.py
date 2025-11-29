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
    creator_id: str = Field(..., description="User ID of the project creator")

# ---------- Update Schema ----------
class ProjectUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100, description="Updated project title")
    description: Optional[str] = Field(None, description="Updated project description")
    skills_required: Optional[List[str]] = Field(default_factory=list, description="Updated skills required")
    status: Optional[str] = Field(None, description="Updated project status")

# ---------- Response Schema ----------
class ProjectOut(ProjectBase):
    id: str
    creator_id: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
