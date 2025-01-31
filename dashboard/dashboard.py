import streamlit as st
import pandas as pd
from data_collection.twitter_data import TwitterDataCollector
from model.sentiment_model import SentimentModel
from data_preprocessing.text_cleaning import TextCleaner  
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Initialize Twitter Data Collector and Sentiment Model
twitter_collector = TwitterDataCollector("AAAAAAAAAAAAAAAAAAAAAI1cygEAAAAA3lM2tn9dMzg4zLrJBaW3HibW6E4%3DsOJ5ZWtx4t6jmuv8c7tv4H0ybPkCZz01u41A2j5fYIYgkgviXE")  # Replace with your actual Bearer Token
sentiment_model = SentimentModel()

def fetch_latest_tweets():
    query = "#YourTopic"  # Replace with the desired topic
    tweets = twitter_collector.collect_tweets(query, max_results=10) 

    tweet_data = []
    for tweet in tweets:
        cleaned_text = TextCleaner.clean_text(tweet['text'])  
        sentiment_result = sentiment_model.predict_sentiment(cleaned_text)  
        
        tweet_data.append({
            "text": tweet['text'],
            "sentiment": sentiment_result["label"],
            "score": sentiment_result["score"],
            "created_at": tweet['created_at']
        })
    
    return pd.DataFrame(tweet_data)  

# Streamlit Dashboard Configuration
st.title("Real-Time Twitter Sentiment Analysis Dashboard")

if st.button("Fetch Latest Tweets"):
    latest_tweets_df = fetch_latest_tweets()
    
    if not latest_tweets_df.empty:
        st.write("### Latest Tweets and Sentiments")
        st.dataframe(latest_tweets_df)

        sentiment_counts = latest_tweets_df['sentiment'].value_counts()
        st.write("### Sentiment Distribution")
        st.bar_chart(sentiment_counts)

        st.write("### Recent Tweets")
        for index, row in latest_tweets_df.iterrows():
            st.write(f"**Tweet:** {row['text']}")
            st.write(f"**Sentiment:** {row['sentiment']} (Score: {row['score']})")
            st.write(f"**Timestamp:** {row['created_at']}")
            st.markdown("---")  

st.markdown("---")
st.write("This dashboard displays real-time sentiment analysis of tweets based on a specified topic.")
