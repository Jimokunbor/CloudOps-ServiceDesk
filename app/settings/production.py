from app.config import settings


class ProductionConfig:
    APP_NAME = settings.APP_NAME
    APP_VERSION = settings.APP_VERSION
    APP_DESCRIPTION = settings.APP_DESCRIPTION

    ENVIRONMENT = "production"

    DEBUG = False

    LOG_LEVEL = "WARNING"