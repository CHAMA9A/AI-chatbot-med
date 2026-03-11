from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.utils.logging import logger
from app.api.routes import router
from app.services.predictor import predictor
from app.services.symptoms import symptom_extractor
from app.services.knowledge_base import knowledge_base


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load model and data at startup, cleanup at shutdown."""
    logger.info("Starting %s v%s", settings.APP_NAME, settings.APP_VERSION)

    # Load model and symptom columns
    predictor.load(settings.MODEL_PATH, settings.TRAINING_CSV_PATH)
    symptom_extractor.load(predictor.symptom_columns)
    knowledge_base.load(settings.DESCRIPTION_CSV_PATH, settings.PRECAUTION_CSV_PATH)

    logger.info("All resources loaded successfully")
    yield
    logger.info("Shutting down")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "AI-powered healthcare chatbot that predicts diseases based on symptoms. "
        f"**Disclaimer:** {settings.DISCLAIMER}"
    ),
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Catch-all handler for unexpected errors."""
    logger.error("Unhandled exception: %s", str(exc), exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal error occurred. Please try again later."},
    )


app.include_router(router)
