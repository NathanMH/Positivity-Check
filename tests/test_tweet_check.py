import unittest
import TweetCheck

class TestTweetCheck(unittest.TestCase):
    """
    Test TweetCheck
    """

    def test_init_without_username(self):
        """
        Test TweetCheck with an empty username string
        """
        username = ""
        twat = TweetCheck.Tweeter(username)

    def test_get_user_tweets_int(self):
        """
        Test get_user_tweets with number that won't exist
        """
        username = "TestTwat"
        twat = TweetCheck.Tweeter(username)
        twat.get_user_tweets(1000000)

    def test_get_user_tweets_str(self):
        """
        Test get_user_tweets with a string???
        """
        twat = TweetCheck.Tweeter("TestTwat")
        twat.get_user_tweets("five")

    def test_get_user_tweets_float(self):
        """
        Test get_user_tweets with a string???
        """
        twat = TweetCheck.Tweeter("TestTwat")
        twat.get_user_tweets(0.381)


if __name__ == '__main__':
    main()
