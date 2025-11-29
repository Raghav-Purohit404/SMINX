import os
from dotenv import load_dotenv

# Load environment variables from .env file at project root
load_dotenv()

# ---------- Database ----------
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./dev.db")

# ---------- JWT Settings ----------
JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret-change-me")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXP_HOURS = int(os.getenv("JWT_EXP_HOURS", "24"))

# ---------- CORS ----------
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# ---------- Debug ----------
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")

