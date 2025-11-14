# app/main.py
from fastapi import FastAPI
from app.routes import user_routes, project_routes, auth_routes
from app.core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Skill Dev Platform API")

# Create tables
Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(user_routes.router, prefix="/api/users", tags=["Users"])
app.include_router(project_routes.router, prefix="/api/projects", tags=["Projects"])
app.include_router(auth_routes.router, prefix="/api/auth", tags=["Auth"])
