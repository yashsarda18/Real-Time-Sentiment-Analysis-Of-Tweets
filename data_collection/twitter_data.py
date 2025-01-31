import tweepy
import time
class TwitterDataCollector:
    def __init__(self, bearer_token):
        """
        Initializes the TwitterDataCollector with a Bearer Token.
        
        Parameters:
            bearer_token (str): The Bearer Token for Twitter API v2.
        """
        self.client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAI1cygEAAAAA3lM2tn9dMzg4zLrJBaW3HibW6E4%3DsOJ5ZWtx4t6jmuv8c7tv4H0ybPkCZz01u41A2j5fYIYgkgviXE")

    def collect_tweets(self, query, max_results=10):
        while True:
            try:
                response = self.client.search_recent_tweets(query=query, max_results=max_results)
                if response.data:
                    tweet_data = [{'text': tweet.text, 'created_at': tweet.created_at} for tweet in response.data]
                    return tweet_data
                else:
                    return []  # Return an empty list if no tweets are found
            except tweepy.TooManyRequests as e:
                print("Rate limit exceeded. Waiting for 15 minutes...")
                time.sleep(15 * 60)  # Wait for 15 minutes before retrying
            except Exception as e:
                print(f"An error occurred: {e}")
                return []  # Handle other exceptions as needed

# Example usage (to be called from main.py)
if __name__ == "__main__":
    collector = TwitterDataCollector("AAAAAAAAAAAAAAAAAAAAAI1cygEAAAAA3lM2tn9dMzg4zLrJBaW3HibW6E4%3DsOJ5ZWtx4t6jmuv8c7tv4H0ybPkCZz01u41A2j5fYIYgkgviXE")  # Replace with your actual Bearer Token
    tweets = collector.collect_tweets("#AI")
    print(tweets)
