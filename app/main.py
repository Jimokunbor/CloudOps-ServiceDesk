from fastapi import FastAPI

from app.api.ticket import router as ticket_router
from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

app.include_router(auth_router)
app.include_router(ticket_router)
app.include_router(health_router)



@app.get("/")
def home():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "status": "Running",
        "environment": settings.ENVIRONMENT,
        "version": settings.APP_VERSION,
    }