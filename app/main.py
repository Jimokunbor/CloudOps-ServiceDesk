from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.api.ticket import router as ticket_router
from app.config import settings
from app.logging.logger import logger
from app.services.redis_service import redis_service
from app.settings import config


app = FastAPI(
    title=config.APP_NAME,
    description=config.APP_DESCRIPTION,
    version=config.APP_VERSION,
)


logger.info(
    f"CloudOps ServiceDesk started in {config.ENVIRONMENT.upper()} mode."
)


if redis_service.ping():
    logger.info("Redis service is available.")


app.include_router(auth_router)
app.include_router(ticket_router)
app.include_router(health_router)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {config.APP_NAME}",
        "status": "Running",
        "environment": config.ENVIRONMENT,
        "version": config.APP_VERSION,
        "debug": config.DEBUG,
    }