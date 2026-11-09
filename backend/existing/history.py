"""Persist generated passwords to disk and provide history/export/statistics."""

import csv
import os
from datetime import datetime

DEFAULT_HISTORY_FILE = os.path.join("data", "history.csv")
FIELDNAMES = ("timestamp", "password", "strength", "length")


def _ensure_history_file(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", newline="", encoding="utf-8") as history_file:
            writer = csv.DictWriter(history_file, fieldnames=FIELDNAMES)
            writer.writeheader()


def save_to_history(password, strength, path=DEFAULT_HISTORY_FILE):
    """Append a generated password with timestamp and strength to the history file."""
    _ensure_history_file(path)

    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "password": password,
        "strength": strength,
        "length": len(password),
    }

    with open(path, "a", newline="", encoding="utf-8") as history_file:
        writer = csv.DictWriter(history_file, fieldnames=FIELDNAMES)
        writer.writerow(entry)

    return entry


def load_history(path=DEFAULT_HISTORY_FILE):
    """Return all saved history entries as a list of dicts, most recent last."""
    if not os.path.exists(path):
        return []

    with open(path, "r", newline="", encoding="utf-8") as history_file:
        reader = csv.DictReader(history_file)
        return list(reader)


def clear_history(path=DEFAULT_HISTORY_FILE):
    """Delete all stored history entries."""
    if os.path.exists(path):
        os.remove(path)


def get_statistics(path=DEFAULT_HISTORY_FILE):
    """Return summary statistics: total generated and average password length."""
    entries = load_history(path)
    if not entries:
        return {"total_generated": 0, "average_length": 0.0}

    lengths = [int(entry["length"]) for entry in entries]
    return {
        "total_generated": len(entries),
        "average_length": round(sum(lengths) / len(lengths), 2),
    }


def export_to_txt(destination, path=DEFAULT_HISTORY_FILE):
    """Export stored passwords (one per line) to a plain text file."""
    entries = load_history(path)
    with open(destination, "w", encoding="utf-8") as export_file:
        for entry in entries:
            export_file.write(f"{entry['password']}\n")

    return len(entries)


def export_to_csv(destination, path=DEFAULT_HISTORY_FILE):
    """Export the full history (timestamp, password, strength, length) to CSV."""
    entries = load_history(path)
    with open(destination, "w", newline="", encoding="utf-8") as export_file:
        writer = csv.DictWriter(export_file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(entries)

    return len(entries)
