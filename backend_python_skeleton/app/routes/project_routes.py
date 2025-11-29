from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.project_service import create_project, get_project, get_all_projects, update_project, delete_project
from app.database import get_db
from app.core.security import get_current_user

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/")
async def create_new_project(data: dict, db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)):
    project = await create_project(db, data)
    return {"message": "Project created", "project": project}

@router.get("/")
async def list_projects(db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return await get_all_projects(db)

@router.get("/{project_id}")
async def read_project(project_id: str, db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)):
    project = await get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}")
async def modify_project(project_id: str, data: dict, db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)):
    updated = await update_project(db, project_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project updated", "project": updated}

@router.delete("/{project_id}")
async def remove_project(project_id: str, db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)):
    deleted = await delete_project(db, project_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted"}

