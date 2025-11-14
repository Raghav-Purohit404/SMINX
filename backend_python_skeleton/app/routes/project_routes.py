from fastapi import APIRouter, HTTPException
from app.services.project_service import (
    create_project, get_project, get_all_projects,
    update_project, delete_project
)

router = APIRouter(prefix="/projects", tags=["Projects"])

# CREATE
@router.post("/")
def create_new_project(data: dict):
    project = create_project(data)
    return {"message": "Project created successfully", "project": project}

# READ ALL
@router.get("/")
def list_projects():
    return get_all_projects()

# READ ONE
@router.get("/{project_id}")
def read_project(project_id: int):
    project = get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# UPDATE
@router.put("/{project_id}")
def modify_project(project_id: int, data: dict):
    updated = update_project(project_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project updated successfully", "project": updated}

# DELETE
@router.delete("/{project_id}")
def remove_project(project_id: int):
    deleted = delete_project(project_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}
