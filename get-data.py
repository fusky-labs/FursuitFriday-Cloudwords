import re
import tweepy
from dotenv import load_dotenv
import os
import json

load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets_list = []

# get the tweets with #fursuitfriday and make sure it's in english and print the text
tweets = api.search_tweets(q='#FursuitFriday', count=100, lang='en')
print(len(tweets))
for index, tweet in enumerate(tweets):
    print(f"tweet:{index}")
    print(tweet.text)
    tweets_list.append(tweet.text)

# replace new lines and emojis with spaces using regex
for i, tweet in enumerate(tweets_list):
    tweets_list[i] = re.sub(r'\n', ' ', tweet)

with open('tweets.json', 'w') as outfile:
    json.dump({"tweets":tweets_list}, outfile)