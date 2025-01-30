from transformers import pipeline

class SentimentModel:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")
    
    def predict_sentiment(self, text):
        result = self.model(text)
        return result[0]

# Example usage (to be called from main.py)
if __name__ == "__main__":
    model = SentimentModel()
    sentiment_result = model.predict_sentiment("I love programming.")
    print(sentiment_result)