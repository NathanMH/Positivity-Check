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
from resources.py_to_file import text_to_file
from resources.py_to_file import file_to_text
from positivity_check import UserText
# Put sensitive keys and tokens into authentication.py file
import resources.authentication as authentication

###################################################################
# 2. FUNCTIONS
###################################################################

CONSUMER_KEY = authentication.CONSUMER_KEY
CONSUMER_SECRET = authentication.CONSUMER_SECRET
ACCESS_TOKEN = authentication.ACCESS_KEY
ACCESS_TOKEN_SECRET = authentication.ACCESS_SECRET


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
        self.tweets_filename = user_id + '.txt'

    def get_user_tweets(self, amount, loc=None):
        """ Retrieve tweets from the user specified. """
        if loc == None:
            if os.path.isfile(self.tweets_filename):
                print('Already collected tweets, retrieving from storage.')
            else:
                try:
                    user_tweets = API.user_timeline(self.user_id, None, None, None, None, amount)
                    for tweet in user_tweets:
                        self.tweets.append(tweet.text.replace('\n', ' '))
                except tweepy.error.TweepError as e:
                    print(e)
        else:
            if os.path.isfile(loc + self.tweets_filename):
                print('Already collected tweets, retrieving from storage.')
            else:
                try:
                    user_tweets = API.user_timeline(self.user_id, None, None, None, None, amount)
                    for tweet in user_tweets:
                        self.tweets.append(tweet.text.replace('\n', ' '))
                except tweepy.error.TweepError as e:
                    print(e)

    # TODO add location parameter (optional)
    def store_tweets(self, loc=None):
        """ Store tweet text in a simple text file. """
        # TODO move to json format
        if loc == None:
            for tweet in self.tweets:
                text_to_file(tweet, self.tweets_filename)
        else:
            for tweet in self.tweets:
                text_to_file(tweet, loc + self.tweets_filename)

    def get_stored_tweets(self, loc=None):
        """ Retrieve tweet text from file. """
        if loc == None:
            self.tweets = file_to_text(self.tweets_filename)
        else:
            self.tweets = file_to_text(loc + self.tweets_filename)

def analyze_tweets(tweets):
    """ Use PositivityCheck module to analyze tweets. """
    tweet_text_objects = []
    for tweet in tweets:
        tweet_object = UserText(tweet)
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
    temp_loc = os.getcwd() + "\\positivity_check\\results\\"
    USERNAME = "NorthernLionLP"
    NUM_OF_TWEETS = 5

    TWIT = Tweeter(USERNAME)
    TWIT.get_user_tweets(NUM_OF_TWEETS, temp_loc)
    TWIT.store_tweets(temp_loc)
    TWIT.get_stored_tweets(temp_loc)
    analyze_tweets(TWIT.tweets)


###################################################################
# 1. TESTING
###################################################################
