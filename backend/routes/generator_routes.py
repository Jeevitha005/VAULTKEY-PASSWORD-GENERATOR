"""Routes for generating passwords and scoring password strength."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas.schemas import (
    GenerateRequest,
    GenerateResponse,
    StrengthRequest,
    StrengthResponse,
)
from services.generator_service import check_password_strength, generate_password_response

router = APIRouter(tags=["generator"])


@router.post("/generate", response_model=GenerateResponse)
def generate(payload: GenerateRequest, db: Session = Depends(get_db)) -> GenerateResponse:
    """Generate a new password using the original CLI's generator logic."""
    try:
        return generate_password_response(payload, db)
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error


@router.post("/strength", response_model=StrengthResponse)
def strength(payload: StrengthRequest) -> StrengthResponse:
    """Score the strength of an arbitrary, client-supplied password."""
    return check_password_strength(payload.password)
