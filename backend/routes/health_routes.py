"""Liveness probe used by monitoring tools and the docker-compose healthcheck."""
from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict:
    """Return a simple status payload confirming the API is running."""
    return {"status": "ok"}
