from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.project_model import Project

# ------------------- Create Project -------------------
async def create_project(db: AsyncSession, data: dict) -> Project:
    new_project = Project(**data)
    db.add(new_project)
    await db.commit()
    await db.refresh(new_project)
    return new_project

# ------------------- Get Project -------------------
async def get_project(db: AsyncSession, project_id: str):
    result = await db.execute(select(Project).where(Project.id == project_id))
    return result.scalar_one_or_none()

# ------------------- Get All Projects -------------------
async def get_all_projects(db: AsyncSession):
    result = await db.execute(select(Project))
    return result.scalars().all()

# ------------------- Update Project -------------------
async def update_project(db: AsyncSession, project_id: str, data: dict):
    project = await get_project(db, project_id)
    if not project:
        return None
    for k, v in data.items():
        setattr(project, k, v)
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project

# ------------------- Delete Project -------------------
async def delete_project(db: AsyncSession, project_id: str):
    project = await get_project(db, project_id)
    if not project:
        return False
    await db.delete(project)
    await db.commit()
    return True
