import logging
from loguru import logger
import sys

def setup_logging(log_file: str = "logs/app.log"):
    """Set up global logging configuration — gọi một lần ở entry point."""
    # Remove default handlers to avoid duplication
    logger.remove()
    # Log ra console
    logger.add(sys.stdout, level="INFO", enqueue=True, colorize=True,
               format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{message}</level>")
    # Log ra file
    logger.add(log_file, rotation="10 MB", retention="7 days", enqueue=True)
    logger.info("✅ Logging configured successfully")

def get_logger(name: str = None):
    """Return logger instance without reconfiguring."""
    return logger.bind(module=name)
