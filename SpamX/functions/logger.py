import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    format="[%(asctime)s]:[%(name)s]:[%(levelname)s] - %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "SpamX.log", maxBytes=(1024 * 1024 * 5), backupCount=10, encoding="utf-8"
        ),
        logging.StreamHandler(),
    ],
)


logging.getLogger("pyrogram").setLevel(logging.ERROR)

LOGS = logging.getLogger("SpamX")