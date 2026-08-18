from datetime import UTC
from datetime import datetime

from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health_check():
    return {
        "status": "healthy",
        "application": "CloudOps ServiceDesk",
        "version": "1.0.0",
        "environment": "development",
        "timestamp": datetime.now(UTC).isoformat(),
    }