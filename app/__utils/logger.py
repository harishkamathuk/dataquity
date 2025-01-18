import logging
import os
from logging.handlers import RotatingFileHandler
from config import Config

# Ensure the logs directory exists
log_dir = os.path.dirname(Config.LOG_FILE_PATH)
os.makedirs(log_dir, exist_ok=True)

# Configure the logger
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO),  # Get log level from config
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(Config.LOG_FILE_PATH, maxBytes=5_000_000, backupCount=3),  # Log file location from config
        logging.StreamHandler(),  # Log to console
    ],
)

def get_logger(name):
    """
    Returns a logger instance with the specified name.
    Args:
        name (str): The name of the logger (usually `__name__`).
    Returns:
        logging.Logger: Configured logger instance.
    """
    return logging.getLogger(name)
