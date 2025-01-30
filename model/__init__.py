from .sentiment_model import SentimentModel
from .api import app  # Import FastAPI app for easy access

__all__ = ["SentimentModel", "app"]  # Expose these components