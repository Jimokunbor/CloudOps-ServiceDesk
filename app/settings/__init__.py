import os

from app.settings.development import DevelopmentConfig
from app.settings.production import ProductionConfig


ENVIRONMENT = os.getenv("ENVIRONMENT", "development").lower()


if ENVIRONMENT == "production":
    config = ProductionConfig()
else:
    config = DevelopmentConfig()