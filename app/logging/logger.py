import logging
import os


LOG_DIRECTORY = "logs"
LOG_FILE = os.path.join(LOG_DIRECTORY, "cloudops.log")

os.makedirs(LOG_DIRECTORY, exist_ok=True)


logger = logging.getLogger("cloudops")

logger.setLevel(logging.INFO)


formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)


console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)


file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)


if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)