"""####################
Author: Nathan Mador-House
Title: Positively Twitter
####################"""

"""####################
Index:
    1. Imports and Readme
    2. Functions
    3. Main
    4. Testing
####################"""


###################################################################
# 1. IMPORTS AND README
###################################################################

import PositivityCheck
import tweepy
import authentication
import py_to_file
import os

###################################################################
# 2. FUNCTIONS
###################################################################

consumer_key = authentication.consumer_key
consumer_secret = authentication.consumer_secret
access_token = authentication.access_token
access_token_secret = authentication.access_secret


def authen():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


class tweeter:

    def __init__(self, user_id):
        self.user_id = user_id
        self.tweets = []
        self.tweets_file = user_id + '.txt'

    def get_user_tweets(self, amount):
        if os.path.isfile(self.tweets_file):
            print('Already collected tweets, retrieving from storage.')
        else:
            user_tweets = api.user_timeline(self.user_id, None, None, None, None, amount)
            for tweet in user_tweets:
                self.tweets.append(tweet.text)

    def store_tweets(self):
        for tweet in self.tweets:
            py_to_file.text_to_file(tweet, self.tweets_file)

    def get_stored_tweets(self):
        self.tweets = py_to_file.file_to_text(self.tweets_file)


def analyze_tweets(tweets):
    tweet_text_objects = []
    for tweet in tweets:
        tweet_object = PositivityCheck.text_block(tweet)
        tweet_text_objects.append(tweet_object)
        print()
        print(tweet.rstrip())
        tweet_object.print_stats()
        # print(tweet_object.sentiment)


def get_home_tweets():
    # Change this to be user_timeline
    public_tweets = api.home_timeline(None, None, 1, None)
    for tweet in public_tweets:
        # print(dir(tweet))
        # print(tweet.user.name + " : " + tweet.text)
        return tweet.text

###################################################################
# 1. MAIN
###################################################################

api = authen()


def __main__(name):
    pass


###################################################################
# 1. TESTING
###################################################################

test = tweeter('NorthernlionLP')
test2 = tweeter('realDonaldTrump')

test2.get_user_tweets(5)
test2.store_tweets()
test2.get_stored_tweets()
print("Setup complete.")
analyze_tweets(test2.tweets)
print("Analyzing Tweets")

