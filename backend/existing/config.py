"""Load and persist user-configurable settings for the password generator."""

import json
import os

CONFIG_PATH = os.path.join("data", "config.json")

DEFAULTS = {
    "default_length": 12,
    "min_length": 6,
    "max_length": 64,
    "use_uppercase": True,
    "use_lowercase": True,
    "use_numbers": True,
    "use_symbols": True,
    "history_file": "data/history.csv",
}


def load_config(path=CONFIG_PATH):
    """Return settings from config.json, falling back to defaults if missing."""
    if not os.path.exists(path):
        save_config(DEFAULTS, path)
        return DEFAULTS.copy()

    with open(path, "r", encoding="utf-8") as config_file:
        try:
            settings = json.load(config_file)
        except json.JSONDecodeError:
            return DEFAULTS.copy()

    merged = DEFAULTS.copy()
    merged.update(settings)
    return merged


def save_config(settings, path=CONFIG_PATH):
    """Write settings to config.json, creating the data folder if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as config_file:
        json.dump(settings, config_file, indent=4)
