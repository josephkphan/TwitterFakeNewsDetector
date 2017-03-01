import xlwt
import tweepy
from tweepy import OAuthHandler
import TweetGatherer.Keys.data

# ---------------- Access Keys ------------------#
consumerKey = TweetGatherer.Keys.data.key['consumerKey']
consumerSecret = TweetGatherer.Keys.data.key['consumerSecret']
accessToken = TweetGatherer.Keys.data.key['accessToken']
accessSecret = TweetGatherer.Keys.data.key['accessSecret']

auth = OAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth)
auth.set_access_token(accessToken, accessSecret)


def get_user_data(username):
    user_data = api.get_user(username)
    # print user_data
    return user_data

# todo write loop to go through an excel file
