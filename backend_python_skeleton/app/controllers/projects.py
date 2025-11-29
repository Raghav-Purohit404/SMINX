# app/controllers/projects.py
from typing import List
from app.schemas.project import ProjectCreate, ProjectOut
from app.services import project_services
from fastapi import HTTPException
from datetime import datetime

async def create_project(payload: ProjectCreate) -> ProjectOut:
    """
    Create a project using the service layer.
    - Accepts a Pydantic ProjectCreate
    - Calls project_services.create_project which persists a SQLAlchemy Project
    - Returns a Pydantic ProjectOut (from ORM)
    """
    # convert to dict for service layer
    data = payload.dict()
    # ensure timestamps if model expects them
    data.setdefault("created_at", datetime.utcnow())
    data.setdefault("updated_at", datetime.utcnow())

    try:
        created = project_services.create_project(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create project: {e}")

    # project_services returns a SQLAlchemy model instance (or similar) — support both dict or orm
    if isinstance(created, dict):
        # simple dict result
        return ProjectOut(**created)
    else:
        # assume SQLAlchemy model with attributes, Pydantic can parse via from_orm
        return ProjectOut.from_orm(created)

