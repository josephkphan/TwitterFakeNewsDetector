import tweepy
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
            tweet = data.split(',"text":"')[1].split('","source')[0]
            userID = data.split(',"id":')[1].split(',"id_str')[0]
            timeStamp = str(time.time())
            print data
            print 'TimeStamp: ' + timeStamp
            print 'Text: ' + tweet
            print 'userID: ' + userID
            print '----------------------'
            return True

        # Could happen with bad internet... etc other errors
        except BaseException, e:
            print 'failed on_data,', str(e)
            time.sleep(5)

    # Happens when an error occurs - probably through a wrong key
    def on_error(self, status):
        print status
        if status == 420:  # 420 means maxed out on number of requests in a window of time
            # returning False in on_data disconnects the stream
            return False


# Setting Authentication Keys for API
auth = OAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth)
auth.set_access_token(accessToken, accessSecret)
twitterStream = Stream(auth, Listener())

# Gathering tweets with keyword Trump
# twitterStream.filter(track=["Trump"])
users = [818568080536178688, 0]
# username = api.lookup_users(users)
# print username

user_data = api.get_user('DylantheOstrich')
print 'Followers: ' + str(user_data.followers_count)
print 'Tweets: ' + str(user_data.statuses_count)
print 'Favourites: ' + str(user_data.favourites_count)
print 'Friends: ' + str(user_data.friends_count)
print 'Appears on ' + str(user_data.listed_count) + ' lists'
# 818568080536178688 DYLANS ID
