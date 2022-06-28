from dotenv import load_dotenv, find_dotenv
import tweepy
import re
import os

load_dotenv(find_dotenv())

auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

tweets_list = []

# get the tweets with #fursuitfriday and make sure it's in english and print the text
tweets = api.search_tweets(q='#FursuitFriday', count=1000, lang='en')
print(len(tweets))
for index, tweet in enumerate(tweets):
    print(f"tweet:{index}")
    print(tweet.text)
    tweets_list.append(tweet.text)

# replace new lines and emojis with spaces using regex
for index, tweet in enumerate(tweets_list):
    tweets_list[index] = re.sub(r'\n', ' ', tweet)
    tweets_list[index] = re.sub(r'[^\x00-\x7F]+', ' ', tweets_list[index])

# TODO: save the tweets to a file, could be in json, or txt