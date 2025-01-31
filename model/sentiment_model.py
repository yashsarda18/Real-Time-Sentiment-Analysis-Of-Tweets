from transformers import pipeline

class SentimentModel:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        """
        Initializes the SentimentModel with a specified pre-trained model.
        
        Parameters:
            model_name (str): The name of the pre-trained model to use.
        """
        # Load the sentiment analysis pipeline with the specified model
        self.model = pipeline("sentiment-analysis", model=model_name)

    def predict_sentiment(self, text):
        """
        Predicts the sentiment of the given text.
        
        Parameters:
            text (str): The input text for sentiment analysis.
        
        Returns:
            dict: A dictionary containing the sentiment label and score.
        """
        result = self.model(text)
        return result[0]  # Return the first result containing label and score

# Example usage (to be called from main.py)
if __name__ == "__main__":
    model = SentimentModel()
    sentiment_result = model.predict_sentiment("I love programming!")
    print(sentiment_result)
