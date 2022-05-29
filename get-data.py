import tweepy
# open api-keys.txt and grab the keys
with open('api-keys.txt', 'r') as f:
    keys = f.read().splitlines()

    consumer_key = keys[0]
    consumer_secret = keys[1]
    access_token = keys[2]
    access_token_secret = keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
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
import re
for index, tweet in enumerate(tweets_list):
    tweets_list[index] = re.sub(r'\n', ' ', tweet)
    tweets_list[index] = re.sub(r'[^\x00-\x7F]+', ' ', tweets_list[index])

# TODO: save the tweets to a file, could be in json, or txt