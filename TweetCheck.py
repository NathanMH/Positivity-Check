#!/usr/bin/python3 
####################
# Author: Nathan Mador-House
# Title: Positively Twitter
####################

####################
# Index:
#     1. Imports and Readme
#     2. Functions
#     3. Main
#     4. Testing
####################


###################################################################
# 1. IMPORTS AND README
###################################################################

import os

import tweepy
import py_to_file

import PositivityCheck
# Put sensitive keys and tokens into authentication.py file
import authentication

###################################################################
# 2. FUNCTIONS
###################################################################

CONSUMER_KEY = authentication.consumer_key
CONSUMER_SECRET = authentication.consumer_secret
ACCESS_TOKEN = authentication.access_token
ACCESS_TOKEN_SECRET = authentication.access_secret


def authen():
    """ Authentication for Twitter. """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api


class Tweeter:
    """ This module is for analyzing tweets from specifi users. It uses the PositivityCheck
    module to to sentiment analysis, currently using the AFINN list of words. """

    def __init__(self, user_id):
        self.user_id = user_id
        self.tweets = []
        self.tweets_file = user_id + '.txt'

    def get_user_tweets(self, amount):
        """ Retrieve tweets from the user specified. """
        if os.path.isfile(self.tweets_file):
            print('Already collected tweets, retrieving from storage.')
        else:
            user_tweets = API.user_timeline(self.user_id, None, None, None, None, amount)
            for tweet in user_tweets:
                self.tweets.append(tweet.text.replace('\n', ' '))

    def store_tweets(self):
        """ Store tweet text in a simple text file. """
        # TODO move to json format
        for tweet in self.tweets:
            py_to_file.text_to_file(tweet, self.tweets_file)

    def get_stored_tweets(self):
        """ Retrieve tweet text from file. """
        self.tweets = py_to_file.file_to_text(self.tweets_file)


def analyze_tweets(tweets):
    """ Use PositivityCheck module to analyze tweets. """
    tweet_text_objects = []
    for tweet in tweets:
        tweet_object = PositivityCheck.UserText(tweet)
        tweet_text_objects.append(tweet_object)
        print()
        print(tweet.rstrip())
        tweet_object.print_stats()


def get_home_tweets(user):
    """ Retrieve tweets from the user home timeline. """
    # TODO make user functional
    # Change this to be user_timeline
    public_tweets = API.home_timeline(None, None, 1, None)
    for tweet in public_tweets:
        return tweet.text

###################################################################
# 1. MAIN
###################################################################

API = authen()


if __name__ == "__main__":
    USERNAME = "NorthernLionLP"
    NUM_OF_TWEETS = 5

    TWIT = Tweeter(USERNAME)
    TWIT.get_user_tweets(NUM_OF_TWEETS)
    TWIT.store_tweets()
    TWIT.get_stored_tweets()
    analyze_tweets(TWIT.tweets)


###################################################################
# 1. TESTING
###################################################################
