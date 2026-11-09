"""Shared pytest fixtures: points the app at an isolated, disposable database."""
import os
import tempfile

_TEST_DB_FD, _TEST_DB_PATH = tempfile.mkstemp(suffix=".db")
os.close(_TEST_DB_FD)

os.environ["DATABASE_URL"] = f"sqlite:///{_TEST_DB_PATH}"
os.environ.setdefault("CORS_ORIGINS", "http://localhost:5173")
