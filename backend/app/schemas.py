from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    """Request body for the /predict endpoint."""
    text: str = Field(
        ...,
        min_length=1,
        description="User's symptom description in natural language",
        examples=["I have a headache and fever"],
    )


class PredictResponse(BaseModel):
    """Successful prediction response."""
    disease: str
    description: str
    precautions: list[str]
    matched_symptoms: list[str]
    disclaimer: str


class HealthResponse(BaseModel):
    """Health check response."""
    status: str = "ok"
    version: str


class ErrorResponse(BaseModel):
    """Standard error response."""
    detail: str
