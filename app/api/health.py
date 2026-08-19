from datetime import UTC
from datetime import datetime

from fastapi import APIRouter

from app.services.background_tasks import send_notification

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health_check():

    send_notification.delay("Health endpoint checked successfully.")

    return {
        "status": "healthy",
        "application": "CloudOps ServiceDesk",
        "version": "1.0.0",
        "environment": "development",
        "timestamp": datetime.now(UTC).isoformat(),
    }