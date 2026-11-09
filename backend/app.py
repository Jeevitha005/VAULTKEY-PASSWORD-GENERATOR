"""FastAPI application entrypoint: app factory, middleware, and routers.

Run with:  uvicorn app:app --reload --port 8000   (from inside backend/)
"""
import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from database import Base, engine  # noqa: E402  (must load env vars first)
from routes import generator_routes, health_routes, history_routes  # noqa: E402

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("password_generator_api")

Base.metadata.create_all(bind=engine)

ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
    if origin.strip()
]

app = FastAPI(
    title="Password Generator API",
    description="REST API that wraps the original password-generator CLI toolkit.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_routes.router, prefix="/api")
app.include_router(generator_routes.router, prefix="/api")
app.include_router(history_routes.router, prefix="/api")


@app.on_event("startup")
def on_startup() -> None:
    """Log a clear message once the API is ready to accept requests."""
    logger.info("Password Generator API started. Docs available at /docs")
