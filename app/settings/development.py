from app.config import settings


class DevelopmentConfig:
    APP_NAME = settings.APP_NAME
    APP_VERSION = settings.APP_VERSION
    APP_DESCRIPTION = settings.APP_DESCRIPTION

    ENVIRONMENT = "development"

    DEBUG = True

    LOG_LEVEL = "INFO"