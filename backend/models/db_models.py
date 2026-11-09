"""Database models backing the password history API."""
from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from database import Base


class PasswordRecord(Base):
    """A single generated password, stored for the history/export endpoints."""

    __tablename__ = "password_history"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=False)
    strength = Column(String(16), nullable=False)
    entropy_bits = Column(Float, nullable=False)
    length = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
