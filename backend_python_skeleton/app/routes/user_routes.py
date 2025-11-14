from fastapi import APIRouter
from app.controllers.users import create_user
from app.models.user import UserCreate

router = APIRouter()

@router.post("/", summary="Create user")
async def create(user: UserCreate):
    return await create_user(user)
