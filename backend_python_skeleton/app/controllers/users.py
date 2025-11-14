from typing import List
from app.models.user import UserCreate, UserOut

async def create_user(payload: UserCreate) -> UserOut:
    # TODO: save to DB
    return UserOut(**payload.dict(), id="fake-id")
