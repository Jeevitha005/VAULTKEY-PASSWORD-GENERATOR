"""Expose the original, unmodified CLI modules as importable Python modules.

The CLI project under ``backend/existing/`` uses plain top-level imports
(``import config``, ``from validator import ...``) because it was written to
run as a standalone script. Rather than editing a single line of that code,
this module puts ``backend/existing/`` on ``sys.path`` so those same imports
resolve correctly when the modules are loaded from inside the FastAPI app.
Every other service imports the legacy modules through this file so the
path setup only has to happen once.
"""
import os
import sys

BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXISTING_DIR = os.path.join(BACKEND_DIR, "existing")

if EXISTING_DIR not in sys.path:
    sys.path.insert(0, EXISTING_DIR)

import generator as legacy_generator  # noqa: E402  (import after sys.path setup, by design)
import history as legacy_history  # noqa: E402
import strength as legacy_strength  # noqa: E402
import utils as legacy_utils  # noqa: E402
from config import load_config  # noqa: E402
from validator import ValidationError  # noqa: E402

HISTORY_CSV_PATH = os.path.join(EXISTING_DIR, "data", "history.csv")
LEGACY_CONFIG_PATH = os.path.join(EXISTING_DIR, "data", "config.json")

__all__ = [
    "legacy_generator",
    "legacy_history",
    "legacy_strength",
    "legacy_utils",
    "load_config",
    "ValidationError",
    "HISTORY_CSV_PATH",
    "LEGACY_CONFIG_PATH",
]
