from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

class LoginSchema(BaseModel):
    email: str

async def login(payload: LoginSchema):
    # TODO: implement real login (JWT + college-domain check)
    if not payload.email.endswith("@college.edu"):
        raise HTTPException(status_code=400, detail="Use college email")
    return {"token": "FAKE-JWT-TOKEN", "email": payload.email}
