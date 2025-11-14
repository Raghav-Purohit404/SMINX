from typing import List
from app.models.project import ProjectCreate, ProjectOut

async def create_project(payload: ProjectCreate) -> ProjectOut:
    # TODO: save to DB
    return ProjectOut(**payload.dict(), id="fake-project-id")
