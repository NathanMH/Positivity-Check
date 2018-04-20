import os
import unittest

from tweet_check import Tweeter


class TestTweetCheck(unittest.TestCase):
    """ Test TweetCheck """

    def test_init_without_username(self):
        """ Test TweetCheck with an empty username string. """
        username = ""
        twat = Tweeter(username)
        self.assertEqual(twat.tweets_filename, username + ".txt")

    def test_get_user_tweets_int(self):
        """ Test get_user_tweets with number that won't exist. """
        username = "TestTwat"
        twat = Tweeter(username)
        twat.get_user_tweets(1000000)

    def test_get_user_tweets_str(self):
        """ Test get_user_tweets with a string? """
        twat = Tweeter("TestTwat")
        twat.get_user_tweets("five")
        self.assertGreater(len(twat.tweets), 0)

    def test_get_user_tweets_float(self):
        """ Test get_user_tweets with a string? """
        twat = Tweeter("TestTwat")
        twat.get_user_tweets(0.381)
        self.assertGreater(len(twat.tweets), 0)

    def test_nonexistant_twat(self):
        """ Test when username provided doesn't exit. """
        twat = Tweeter("TestTwat291sr03")
        twat.get_user_tweets(1)

    def test_tweet_saving(self):
        """ Test saving the tweets to a file TODO Move to json """
        twat = Tweeter("TestTwat")
        twat.get_user_tweets(1)
        twat.store_tweets(os.getcwd() + "\\positivity_check\\results\\")
        self.assertEqual(os.path.isfile(os.getcwd() + "\\positivity_check\\results\\" + twat.tweets_filename), True)

if __name__ == '__main__':
    pass
