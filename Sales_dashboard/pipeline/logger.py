import logging
import os

# create log folder if not exists
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("pipeline")
logger.setLevel(logging.INFO)

# create file handler
file_handler = logging.FileHandler("logs/pipeline.log")

# log format
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)

# attach handler to logger
logger.addHandler(file_handler)