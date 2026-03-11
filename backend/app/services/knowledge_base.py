import csv
from app.utils.logging import logger


class KnowledgeBase:
    """Loads and serves disease descriptions and precautions from CSV files."""

    def __init__(self):
        self.descriptions: dict[str, str] = {}
        self.precautions: dict[str, list[str]] = {}

    def load(self, description_path: str, precaution_path: str) -> None:
        """Load description and precaution CSVs into memory."""
        # Load descriptions
        with open(description_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    disease = row[0].strip()
                    desc = row[1].strip()
                    self.descriptions[disease] = desc

        logger.info("Loaded %d disease descriptions", len(self.descriptions))

        # Load precautions
        with open(precaution_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    disease = row[0].strip()
                    precs = [p.strip() for p in row[1:] if p.strip()]
                    self.precautions[disease] = precs

        logger.info("Loaded %d disease precautions", len(self.precautions))

    def get_description(self, disease: str) -> str:
        return self.descriptions.get(disease, "No description available.")

    def get_precautions(self, disease: str) -> list[str]:
        return self.precautions.get(disease, [])


knowledge_base = KnowledgeBase()
