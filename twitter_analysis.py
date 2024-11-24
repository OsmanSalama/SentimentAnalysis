import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up your API keys and tokens from Twitter Developer Portal
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

# Initialize the client with bearer token (preferred for v2 API)
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True
)

# Define the search query
search_query = "europe refugees lang:en"

try:
    # Verify credentials first
    print("Verifying credentials...")

    # Search tweets using v2 endpoint
    print("Searching for tweets...")
    tweets = client.search_recent_tweets(
        query=search_query,
        max_results=10,
        tweet_fields=['created_at', 'author_id']  # Request additional tweet fields
    )

    # Print the tweets
    if tweets.data:
        for tweet in tweets.data:
            print(f"Tweet ID: {tweet.id}")
            print(f"Created at: {tweet.created_at}")
            print(f"Content: {tweet.text}")
            print("-" * 50)
    else:
        print("No tweets found")

except tweepy.TweepyException as e:
    print(f"Error occurred: {str(e)}")
    print("\nDebugging information:")
    print("1. Check if your bearer token is correct")
    print("2. Verify that your app has Read permissions enabled")
    print("3. Make sure your OAuth 1.0a tokens are valid")