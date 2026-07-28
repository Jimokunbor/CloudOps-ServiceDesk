from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")
    APP_DESCRIPTION = os.getenv("APP_DESCRIPTION")

    APP_HOST = os.getenv("APP_HOST")
    APP_PORT = int(os.getenv("APP_PORT", 8000))

    ENVIRONMENT = os.getenv("ENVIRONMENT")
    DEBUG = os.getenv("DEBUG") == "True"

    DATABASE_URL = os.getenv("DATABASE_URL")

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    )


settings = Settings()