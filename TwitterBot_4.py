# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "ho0syaVOcYapNnj2gtCFfF5io"
consumer_secret = "WN5xsDa2ufNVPR9MPJkHxVwTSxREYY8JxMG6sI8tQ8wrHDmITW"
access_token = "907733914470567937-7Us4vjLpARCIOrJCZoYLqBxVMqYPUUU"
access_token_secret = "ypNiR5CCZQn8clBmeX25glfGi07ZuEUiJw4xxcX319KuV"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "TwitterBot Test" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1