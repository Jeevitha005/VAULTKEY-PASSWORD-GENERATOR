"""Small shared helpers used across the project: clipboard access and logging."""

import logging
import os

LOG_PATH = os.path.join("data", "app.log")


def setup_logger(name="password_generator", log_path=LOG_PATH):
    """Configure and return a logger that writes to data/app.log."""
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(log_path, encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def copy_to_clipboard(text):
    """Copy text to the system clipboard. Returns True on success, False otherwise."""
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except Exception:
        return False
