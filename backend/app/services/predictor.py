import pickle
import numpy as np
import pandas as pd
from app.utils.logging import logger


class Predictor:
    """Loads the trained model and makes disease predictions."""

    def __init__(self):
        self.model = None
        self.symptom_columns: list[str] = []

    def load(self, model_path: str, training_csv_path: str) -> None:
        """Load the pickled model and extract symptom column order from Training.csv."""
        # Load model
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)
        logger.info("Model loaded from %s", model_path)

        # Extract symptom columns (all columns except the last 'prognosis' column)
        df = pd.read_csv(training_csv_path, nrows=0)
        self.symptom_columns = [c.strip() for c in df.columns.tolist()[:-1]]
        logger.info("Extracted %d symptom columns from training data", len(self.symptom_columns))

    def predict(self, feature_vector: list[int]) -> str:
        """Predict disease from a binary feature vector."""
        arr = np.array(feature_vector).reshape(1, -1)
        prediction = self.model.predict(arr)
        disease = prediction[0]
        logger.info("Predicted disease: %s", disease)
        return str(disease)


predictor = Predictor()
