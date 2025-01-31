import nltk
# Download necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
from data_collection.twitter_data import TwitterDataCollector 
from data_preprocessing.text_cleaning import TextCleaner 
from data_preprocessing.tokenisation import Tokeniser 
from model.sentiment_model import SentimentModel 
import time 

def main():
    twitter_collector = TwitterDataCollector("AAAAAAAAAAAAAAAAAAAAAI1cygEAAAAA3lM2tn9dMzg4zLrJBaW3HibW6E4%3DsOJ5ZWtx4t6jmuv8c7tv4H0ybPkCZz01u41A2j5fYIYgkgviXE")  # Replace with your actual Bearer Token
    
    while True:
        tweets = twitter_collector.collect_tweets("#AI")  # Replace with desired topic
        
        for tweet in tweets:
            cleaned_text = TextCleaner.clean_text(tweet['text'])
            tokens = Tokeniser.tokenise(cleaned_text)

            model = SentimentModel()
            sentiment_result = model.predict_sentiment(cleaned_text)

            print(f"Tweet: {tweet['text']}, Sentiment: {sentiment_result['label']}, Score: {sentiment_result['score']}")

        time.sleep(1)  # Collect new tweets every second

if __name__ == "__main__":
    main()
