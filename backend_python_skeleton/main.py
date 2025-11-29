# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from app.routes import user_routes, project_routes
from app.routes.auth_routes import router as auth_router  # auth routes

# Import database
from app.core.database import Base, engine

app = FastAPI(title="SMNIX - Skill Matching Platform")

# ----------------- Database Setup -----------------
# Create tables (sync for startup, works with async sessions later)
Base.metadata.create_all(bind=engine)

# ----------------- CORS -----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- Include Routers -----------------
app.include_router(user_routes.router, prefix="/api/users", tags=["Users"])
app.include_router(project_routes.router, prefix="/api/projects", tags=["Projects"])
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])

# ----------------- Root -----------------
@app.get("/")
async def root():
    return {"message": "Welcome to SMNIX API"}
