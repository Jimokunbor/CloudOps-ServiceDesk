from app.config import settings


class AIConfig:
    PROVIDER = "openai"

    MODEL = "gpt-4.1-mini"

    TEMPERATURE = 0.2

    MAX_TOKENS = 1000

    TIMEOUT = 60

    ENABLE_AI = True

    APP_NAME = settings.APP_NAME