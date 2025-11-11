# common/logger/logger.py
import logging
import sys

def setup_logging(level=logging.INFO):
    """Configure global logging once at application entry point."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

def get_logger(name: str):
    """Return a namespaced logger (no reconfiguration)."""
    return logging.getLogger(name)