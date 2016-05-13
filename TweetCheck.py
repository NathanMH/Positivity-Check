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

class tweeter(user_id):
    tweet_text_objects = []
    def __init__(self):
        self.tweets_text = []

        self.get_user_tweets()
        self.analyze_tweets()

    def get_user_tweets(self):
        user_tweets = api.user_timeline(user_id)
        for tweet in user_tweets:
           self.tweets_text.append(tweet.text)

    # Creates the tweet objects from just the text
    def analyze_tweets(self):
        for tweet in self.tweets:
            tweet_object = PositivityCheck.text_block(tweet)
            tweet_text_objects.append(tweet_object)
            tweet_object.print_stats()

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

real_test_tweet = "RT @ott_ecodistrict: La famille Germain w @JimWatsonOttawa at the opening of a great, green hotel in the EcoDistrict @cmckenney https://t.c…"

print(get_tweets())

#print(real_test_tweet)
tweet_positivity(real_test_tweet)



