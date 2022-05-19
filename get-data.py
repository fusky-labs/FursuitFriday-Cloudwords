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
