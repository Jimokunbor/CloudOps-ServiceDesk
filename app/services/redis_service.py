import redis

from app.logging.logger import logger


class RedisService:
    def __init__(self):
        self.client = redis.Redis(
            host="redis",
            port=6379,
            decode_responses=True,
        )

    def ping(self):
        try:
            if self.client.ping():
                logger.info("Redis connection established successfully.")
                return True
        except Exception as error:
            logger.error(f"Redis connection failed: {error}")
            return False


redis_service = RedisService()