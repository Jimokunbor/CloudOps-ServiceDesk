from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "status": "Running",
        "environment": settings.ENVIRONMENT,
        "version": settings.APP_VERSION,
    }