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

    public_tweets = api.home_timeline(None, None, 1, None)
    for tweet in public_tweets:
        # print(dir(tweet))
        # print(tweet.user.name + " : " + tweet.text)
        return tweet.text

def tweet_positivity(tweet):
    text = PositivityCheck.text_block(tweet)
    text.print_stats()

###################################################################
# 1. MAIN
###################################################################

###################################################################
# 1. TESTING
###################################################################

#test_tweet = authen()
real_test_tweet = "RT @ott_ecodistrict: La famille Germain w @JimWatsonOttawa at the opening of a great, green hotel in the EcoDistrict @cmckenney https://t.c…"
 

print(real_test_tweet)
tweet_positivity(real_test_tweet)



