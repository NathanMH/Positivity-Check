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

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print()
        # print(dir(tweet))
        print(tweet.user.name + " : " + tweet.text)
        print()


def tweet_positivity(tweet):
    text = PositivityCheck.text_block

###################################################################
# 1. MAIN
###################################################################

###################################################################
# 1. TESTING
###################################################################

authen()



