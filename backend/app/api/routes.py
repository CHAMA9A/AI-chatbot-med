from fastapi import APIRouter, HTTPException
from app.schemas import PredictRequest, PredictResponse, HealthResponse, ErrorResponse
from app.services.predictor import predictor
from app.services.symptoms import symptom_extractor
from app.services.knowledge_base import knowledge_base
from app.core.config import settings
from app.utils.logging import logger

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(status="ok", version=settings.APP_VERSION)


@router.post(
    "/predict",
    response_model=PredictResponse,
    responses={422: {"model": ErrorResponse}},
)
async def predict(request: PredictRequest):
    """
    Predict disease from symptom description.

    Accepts natural language text describing symptoms and returns the predicted
    disease along with its description and recommended precautions.
    """
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=422, detail="Input text cannot be empty.")

    # Extract symptoms
    vector, matched = symptom_extractor.extract(text)

    if not matched:
        logger.warning("No symptoms detected in input: '%s'", text[:100])
        raise HTTPException(
            status_code=422,
            detail=(
                "No recognizable symptoms found in your input. "
                "Try describing specific symptoms like: headache, fever, cough, fatigue, nausea, skin rash, etc."
            ),
        )

    logger.info("Matched %d symptoms: %s", len(matched), matched)

    # Predict
    disease = predictor.predict(vector)

    # Enrich with knowledge base
    description = knowledge_base.get_description(disease)
    precautions = knowledge_base.get_precautions(disease)

    return PredictResponse(
        disease=disease,
        description=description,
        precautions=precautions,
        matched_symptoms=matched,
        disclaimer=settings.DISCLAIMER,
    )
