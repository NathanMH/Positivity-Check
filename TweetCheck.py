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
        self.get_user_tweets()

    def get_user_tweets(self):
        user_tweets = api.user_timeline(self.user_id, None, None, None, None, 7)
        for tweet in user_tweets:
            self.tweets.append(tweet.text)


def analyze_tweets(tweeter):  # Creates the tweet objects from just the text
    # Changing this to not take a tweeter object, just takes text
    tweet_text_objects = []
    for tweet in tweeter.tweets:
        tweet_object = PositivityCheck.text_block(tweet)
        tweet_text_objects.append(tweet_object)
        print(tweet)
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

# real_test_tweet = "@JimWatsonOttawa test tweet!"
# print(real_test_tweet)

# test = tweeter('NorthernlionLP')
test2 = tweeter('realDonaldTrump')

# Testing the text to and from a file
py_to_file.text_to_file(test2.tweets, 'written_file.txt')
py_to_file.file_to_text()

