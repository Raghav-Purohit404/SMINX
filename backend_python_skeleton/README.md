# Backend Skeleton (FastAPI)

This is a starter skeleton for the backend (Python + FastAPI) of your College Project Team Builder app.

## Structure
- `app/` - FastAPI application code
  - `controllers/` - business logic functions
  - `models/` - Pydantic models (request/response)
  - `routes/` - FastAPI routers
  - `middleware/` - auth / role middleware
  - `utils/` - helpers (email, files...)
- `requirements.txt` - pip dependencies
- `.env.example` - environment variables example

## Run (development)
1. Create a virtualenv and install requirements
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run with uvicorn
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
