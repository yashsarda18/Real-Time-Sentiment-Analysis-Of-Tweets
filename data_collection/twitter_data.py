import tweepy

class TwitterDataCollector:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        self.auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        self.api = tweepy.API(self.auth)
        
    def collect_tweets(self, query, count=100):
        tweets = self.api.search_tweets(q=query, lang="en", count=count)
        tweet_data = [{'text': tweet.text, 'created_at': tweet.created_at} for tweet in tweets]
        return tweet_data

# Example usage (to be called from main.py)
if __name__ == "__main__":
    collector = TwitterDataCollector("your_api_key", "your_api_secret_key", "your_access_token", "your_access_token_secret")
    tweets = collector.collect_tweets("#YourTopic")
    print(tweets)