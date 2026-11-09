"""Request and response models exposed by the REST API."""
from datetime import datetime

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    """Options accepted by POST /api/generate, mirroring the CLI's own prompts."""

    length: int = Field(default=12, ge=1, le=256)
    min_length: int = Field(default=6, ge=1)
    max_length: int = Field(default=64, ge=1)
    use_uppercase: bool = True
    use_lowercase: bool = True
    use_numbers: bool = True
    use_symbols: bool = True
    exclude_ambiguous: bool = False


class GenerateResponse(BaseModel):
    """A freshly generated password along with its strength metadata."""

    id: int
    password: str
    strength: str
    entropy_bits: float
    length: int
    score: int
    estimated_crack_time: str
    created_at: datetime

    class Config:
        from_attributes = True


class StrengthRequest(BaseModel):
    """Payload for POST /api/strength: an arbitrary password to evaluate."""

    password: str = Field(..., min_length=1)


class StrengthResponse(BaseModel):
    """Strength metadata for a password supplied by the client."""

    password_length: int
    entropy_bits: float
    strength: str
    score: int
    estimated_crack_time: str


class HistoryResponse(BaseModel):
    """A single stored history record returned by GET /api/history."""

    id: int
    password: str
    strength: str
    entropy_bits: float
    length: int
    created_at: datetime

    class Config:
        from_attributes = True
