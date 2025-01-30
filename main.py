from data_collection.twitter_data import TwitterDataCollector 
from data_preprocessing.text_cleaning import TextCleaner 
from data_preprocessing.tokenisation import Tokeniser 
from model.sentiment_model import SentimentModel 
import time 

def main():
    twitter_collector = TwitterDataCollector("fPydoBCmaE0LmRPo3xGYeoMBr", "NwWke3tbRWE2vcVWFXkwPCUwEhb6uPPGKuCGDFmrIlOpkCzvls", "1884883958372188160-m8IZKEU7ALIz4WsLBGWQsekwM4X9BN", "SPTPf1QvKPBg9HOrCFhV10h2lIFbfJqzJbYc69iYpcjYK")
    
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