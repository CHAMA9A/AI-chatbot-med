import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    APP_NAME: str = "AI Healthcare Chatbot"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Paths relative to backend/ directory
    DATA_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
    MODEL_PATH: str = ""
    TRAINING_CSV_PATH: str = ""
    DESCRIPTION_CSV_PATH: str = ""
    PRECAUTION_CSV_PATH: str = ""

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    DISCLAIMER: str = (
        "This tool is for educational purposes only and does NOT provide medical advice. "
        "Always consult a qualified healthcare professional for medical concerns."
    )

    class Config:
        env_file = ".env"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.MODEL_PATH:
            self.MODEL_PATH = os.path.join(self.DATA_DIR, "model.pkl")
        if not self.TRAINING_CSV_PATH:
            self.TRAINING_CSV_PATH = os.path.join(self.DATA_DIR, "Training.csv")
        if not self.DESCRIPTION_CSV_PATH:
            self.DESCRIPTION_CSV_PATH = os.path.join(self.DATA_DIR, "symptom_Description.csv")
        if not self.PRECAUTION_CSV_PATH:
            self.PRECAUTION_CSV_PATH = os.path.join(self.DATA_DIR, "symptom_precaution.csv")


settings = Settings()
