from fastapi import APIRouter, Depends
from app.controllers import auth as auth_ctrl
from app.controllers.auth import LoginSchema

router = APIRouter()

@router.post("/login")
async def login(payload: LoginSchema):
    return await auth_ctrl.login(payload)
