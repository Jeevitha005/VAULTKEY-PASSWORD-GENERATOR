"""Business logic for password generation and strength scoring.

All actual password generation and entropy/strength math is delegated to the
untouched legacy modules in ``backend/existing/``. This file only adapts
those results into API responses and adds display-only extras (a 0-100 score
and a human-readable crack-time estimate) that do not alter the legacy
algorithms in any way.
"""
from datetime import datetime

from sqlalchemy.orm import Session

from models.db_models import PasswordRecord
from schemas.schemas import GenerateRequest, GenerateResponse, StrengthResponse
from services.legacy_bridge import (
    HISTORY_CSV_PATH,
    ValidationError,
    legacy_generator,
    legacy_history,
    legacy_strength,
)

# Guesses per second assumed for an offline, GPU-assisted attacker. Used only
# to render the "estimated crack time" string shown in the UI.
GUESSES_PER_SECOND = 1_000_000_000

_TIME_UNITS = (
    ("century", 60 * 60 * 24 * 365 * 100),
    ("year", 60 * 60 * 24 * 365),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("minute", 60),
    ("second", 1),
)


def _humanize_seconds(seconds: float) -> str:
    """Convert a duration in seconds into a short, human-readable phrase."""
    if seconds < 1:
        return "instantly"

    for unit_name, unit_seconds in _TIME_UNITS:
        value = seconds / unit_seconds
        if value >= 1:
            if unit_name == "century" and value > 1_000:
                return "trillions of years"
            rounded = round(value, 1)
            plural = "" if rounded == 1 else "s"
            return f"{rounded} {unit_name}{plural}"

    return "instantly"


def _estimate_crack_time(entropy_bits: float) -> str:
    """Estimate offline brute-force crack time from an entropy value in bits."""
    if entropy_bits <= 0:
        return "instantly"

    seconds = (2 ** entropy_bits) / GUESSES_PER_SECOND
    return _humanize_seconds(seconds)


def _score_from_entropy(entropy_bits: float) -> int:
    """Map entropy bits onto a 0-100 score used to animate the strength bar."""
    return max(0, min(100, round((entropy_bits / 128) * 100)))


def generate_password_response(payload: GenerateRequest, db: Session) -> GenerateResponse:
    """Generate a password with the legacy generator and persist it to history.

    Raises:
        ValueError: if the requested options fail legacy validation.
    """
    try:
        password = legacy_generator.generate_password(
            length=payload.length,
            min_length=payload.min_length,
            max_length=payload.max_length,
            use_uppercase=payload.use_uppercase,
            use_lowercase=payload.use_lowercase,
            use_numbers=payload.use_numbers,
            use_symbols=payload.use_symbols,
            exclude_ambiguous=payload.exclude_ambiguous,
        )
    except ValidationError as error:
        raise ValueError(str(error)) from error

    report = legacy_strength.strength_report(password)

    # Keep the original CLI's CSV history file working exactly as it did before.
    legacy_history.save_to_history(password, report["strength"], HISTORY_CSV_PATH)

    # Also persist a normalized row that powers this web app's own history API.
    record = PasswordRecord(
        password=password,
        strength=report["strength"],
        entropy_bits=report["entropy_bits"],
        length=report["password_length"],
        created_at=datetime.utcnow(),
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return GenerateResponse(
        id=record.id,
        password=password,
        strength=report["strength"],
        entropy_bits=report["entropy_bits"],
        length=report["password_length"],
        score=_score_from_entropy(report["entropy_bits"]),
        estimated_crack_time=_estimate_crack_time(report["entropy_bits"]),
        created_at=record.created_at,
    )


def check_password_strength(password: str) -> StrengthResponse:
    """Return a strength report for an arbitrary, user-supplied password."""
    report = legacy_strength.strength_report(password)
    return StrengthResponse(
        password_length=report["password_length"],
        entropy_bits=report["entropy_bits"],
        strength=report["strength"],
        score=_score_from_entropy(report["entropy_bits"]),
        estimated_crack_time=_estimate_crack_time(report["entropy_bits"]),
    )
