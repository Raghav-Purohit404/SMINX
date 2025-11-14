from app.models.project_model import Project
from app.core.database import SessionLocal

# CREATE
def create_project(data):
    db = SessionLocal()
    new_project = Project(**data)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    db.close()
    return new_project

# READ (by id)
def get_project(project_id: int):
    db = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    db.close()
    return project

# READ ALL
def get_all_projects():
    db = SessionLocal()
    projects = db.query(Project).all()
    db.close()
    return projects

# UPDATE
def update_project(project_id: int, data: dict):
    db = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        db.close()
        return None
    for key, value in data.items():
        setattr(project, key, value)
    db.commit()
    db.refresh(project)
    db.close()
    return project

# DELETE
def delete_project(project_id: int):
    db = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        db.close()
        return None
    db.delete(project)
    db.commit()
    db.close()
    return True
