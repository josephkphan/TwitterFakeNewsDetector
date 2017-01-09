from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# ------------Keys for API---------- #
consumerKey = 'eOOgZZpX8hmaPxIn0VoRbECil'
consumerSecret = '7rLhBiVALul0IYKcqbx0DRBajzPtYofO5Iw2Szv25rWhqmXFkW'
accessToken = '818157828921667584-6cTUK2RvwKdjpRevQ7msUE22sLcUUJi'
accessSecret = 'SZBZKw10OAINbqQaCp5ZzUgQDXRPNkI2UhHDACmwafdIO'


# Creating Listener class that will gather data from API
class Listener(StreamListener):
    def on_data(self, data):
        print data
        return True

    # Happens when an error occurs
    def on_error(self, status):
        print status

# Setting Authentication Keys for API
auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)
twitterStream = Stream(auth, Listener())

# Gathering tweets with keyword Trump
twitterStream.filter(track=["Trump"])
