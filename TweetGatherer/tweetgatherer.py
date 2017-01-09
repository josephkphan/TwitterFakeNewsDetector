from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import key
import time

# ------------Keys for API---------- #
consumerKey = key.consumerKey
consumerSecret = key.consumerSecret
accessToken = key.accessToken
accessSecret = key.accessSecret


# Creating Listener class that will gather data from API
class Listener(StreamListener):

    # Authentication worked and getting data
    def on_data(self, data):
        try:
            print data
            return True

        # Could happen with bad internet... etc other errors
        except BaseException, e:
            print 'failed on_data,', str(e)
            time.sleep(5)

    # Happens when an error occurs - probably through a wrong key
    def on_error(self, status):
        print status

# Setting Authentication Keys for API
auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)
twitterStream = Stream(auth, Listener())

# Gathering tweets with keyword Trump
twitterStream.filter(track=["Trump"])
