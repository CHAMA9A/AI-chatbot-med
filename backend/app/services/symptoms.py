from app.utils.logging import logger


class SymptomExtractor:
    """Extracts symptoms from user text using keyword matching against known symptom columns."""

    def __init__(self):
        self.symptom_columns: list[str] = []
        # Map: cleaned name (spaces) -> original column name (underscores)
        self.symptom_lookup: dict[str, str] = {}

    def load(self, symptom_columns: list[str]) -> None:
        """Initialize with symptom column names from Training.csv."""
        self.symptom_columns = symptom_columns
        self.symptom_lookup = {}
        for col in symptom_columns:
            clean = col.strip().replace("_", " ").lower()
            self.symptom_lookup[clean] = col
        logger.info("Loaded %d symptom features", len(self.symptom_columns))

    def extract(self, text: str) -> tuple[list[int], list[str]]:
        """
        Extract symptoms from user text.
        Returns (feature_vector, matched_symptom_names).
        """
        text_lower = text.lower().strip()
        vector = [0] * len(self.symptom_columns)
        matched: list[str] = []

        for clean_name, original_col in self.symptom_lookup.items():
            if clean_name in text_lower:
                idx = self.symptom_columns.index(original_col)
                vector[idx] = 1
                matched.append(clean_name)

        return vector, matched


symptom_extractor = SymptomExtractor()
