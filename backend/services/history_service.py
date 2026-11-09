"""Database-backed history operations exposed through the REST API.

Reads and writes the SQLite table used by the web app's history/export
endpoints. This is intentionally separate from the legacy CSV history file
in ``backend/existing/data/history.csv``, which keeps recording every
generated password exactly as the original CLI project always has.
"""
import csv
import os

from sqlalchemy.orm import Session

from models.db_models import PasswordRecord

BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT_DIR = os.path.join(BACKEND_DIR, "static", "exports")
os.makedirs(EXPORT_DIR, exist_ok=True)


def list_history(db: Session, limit: int = 50):
    """Return the most recently generated passwords, newest first."""
    return (
        db.query(PasswordRecord)
        .order_by(PasswordRecord.created_at.desc())
        .limit(limit)
        .all()
    )


def clear_all_history(db: Session) -> int:
    """Delete every stored history record and return how many were removed."""
    count = db.query(PasswordRecord).delete()
    db.commit()
    return count


def export_history_txt(db: Session) -> str:
    """Write all stored passwords, one per line, to a .txt file; return its path."""
    records = db.query(PasswordRecord).order_by(PasswordRecord.created_at.desc()).all()
    file_path = os.path.join(EXPORT_DIR, "passwords.txt")

    with open(file_path, "w", encoding="utf-8") as export_file:
        for record in records:
            export_file.write(f"{record.password}\n")

    return file_path


def export_history_csv(db: Session) -> str:
    """Write the full history table to a .csv file and return its path."""
    records = db.query(PasswordRecord).order_by(PasswordRecord.created_at.desc()).all()
    file_path = os.path.join(EXPORT_DIR, "passwords.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as export_file:
        writer = csv.writer(export_file)
        writer.writerow(["id", "password", "strength", "entropy_bits", "length", "created_at"])
        for record in records:
            writer.writerow([
                record.id,
                record.password,
                record.strength,
                record.entropy_bits,
                record.length,
                record.created_at.isoformat(),
            ])

    return file_path
