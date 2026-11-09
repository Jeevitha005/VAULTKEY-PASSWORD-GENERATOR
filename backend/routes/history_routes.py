"""Routes for browsing, clearing, and exporting password history."""
from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from database import get_db
from schemas.schemas import HistoryResponse
from services.history_service import (
    clear_all_history,
    export_history_csv,
    export_history_txt,
    list_history,
)

router = APIRouter(tags=["history"])


@router.get("/history", response_model=List[HistoryResponse])
def get_history(limit: int = 50, db: Session = Depends(get_db)):
    """Return the most recently generated passwords, newest first."""
    return list_history(db, limit)


@router.delete("/history")
def delete_history(db: Session = Depends(get_db)):
    """Delete all stored password history and report how many rows were removed."""
    deleted = clear_all_history(db)
    return {"deleted": deleted}


@router.get("/export/txt")
def export_txt(db: Session = Depends(get_db)) -> FileResponse:
    """Export all history passwords as a downloadable .txt file."""
    file_path = export_history_txt(db)
    return FileResponse(file_path, filename="passwords.txt", media_type="text/plain")


@router.get("/export/csv")
def export_csv(db: Session = Depends(get_db)) -> FileResponse:
    """Export the full password history as a downloadable .csv file."""
    file_path = export_history_csv(db)
    return FileResponse(file_path, filename="passwords.csv", media_type="text/csv")
