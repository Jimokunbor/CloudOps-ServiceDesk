from app.celery import celery_app
from app.logging.logger import logger


@celery_app.task
def send_notification(message: str) -> str:
    logger.info(f"Background notification: {message}")
    return f"Notification processed: {message}"