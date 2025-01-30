import streamlit as st
import pandas as pd
import requests
from data_collection.twitter_data import TwitterDataCollector
from model.sentiment_model import SentimentModel
from data_preprocessing.text_cleaning import TextCleaner

# Initialize Twitter Data Collector and Sentiment Model
twitter_collector = TwitterDataCollector("your_api_key", "your_api_secret_key", "your_access_token", "your_access_token_secret")
sentiment_model = SentimentModel()

def fetch_latest_tweets():
    """
    Fetch the latest tweets and their sentiments.
    
    Returns:
        DataFrame: A DataFrame containing tweets, their sentiments, and scores.
    """
    query = "#YourTopic"  # Replace with the desired topic
    tweets = twitter_collector.collect_tweets(query, count=10)  # Fetch latest tweets (adjust count as needed)

    tweet_data = []
    for tweet in tweets:
        cleaned_text = TextCleaner.clean_text(tweet['text'])  # Clean the tweet text
        sentiment_result = sentiment_model.predict_sentiment(cleaned_text)  # Predict sentiment
        
        tweet_data.append({
            "text": tweet['text'],
            "sentiment": sentiment_result["label"],
            "score": sentiment_result["score"],
            "created_at": tweet['created_at']
        })
    
    return pd.DataFrame(tweet_data)  # Return as a DataFrame

# Streamlit Dashboard Configuration
st.title("Real-Time Twitter Sentiment Analysis Dashboard")

if st.button("Fetch Latest Tweets"):
    latest_tweets_df = fetch_latest_tweets()
    
    if not latest_tweets_df.empty:
        st.write("### Latest Tweets and Sentiments")
        st.dataframe(latest_tweets_df)

        # Display sentiment distribution
        sentiment_counts = latest_tweets_df['sentiment'].value_counts()
        st.write("### Sentiment Distribution")
        st.bar_chart(sentiment_counts)

        # Display recent tweets with sentiments
        st.write("### Recent Tweets")
        for index, row in latest_tweets_df.iterrows():
            st.write(f"**Tweet:** {row['text']}")
            st.write(f"**Sentiment:** {row['sentiment']} (Score: {row['score']})")
            st.write(f"**Timestamp:** {row['created_at']}")
            st.markdown("---")  # Separator line

# Footer Information
st.markdown("---")
st.write("This dashboard displays real-time sentiment analysis of tweets based on a specified topic.")
