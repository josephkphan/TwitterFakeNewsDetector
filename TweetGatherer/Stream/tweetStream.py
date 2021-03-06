import json
import time

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

import TweetGatherer.Keys.data
import TweetGatherer.Keys.dataLoader

# ------------Keys for API---------- #

consumerKey = TweetGatherer.Keys.data.key['consumerKey']
consumerSecret = TweetGatherer.Keys.data.key['consumerSecret']
accessToken = TweetGatherer.Keys.data.key['accessToken']
accessSecret = TweetGatherer.Keys.data.key['accessSecret']

print TweetGatherer.Keys.data.fileTrackerData


# Creating Listener class that will gather data from API
class Listener(StreamListener):
    # Authentication worked and getting data

    def on_data(self, str_data):
        try:
            # data from on_data initially comes in as string. Converts to json
            # print str_data
            data_json = json.loads(str_data)

            # Checking if keys exist in data
            if 'id' in data_json and 'text' in data_json and 'user' in data_json:
                try:
                    # if data.fileTrackerData['tweetNum'] % 1000 == 0:
                    #     data.fileTrackerData['tweetNum'] += 1
                    #     time.sleep(100)
                    fileNum = int(TweetGatherer.Keys.data.fileTrackerData['tweetNum'] / 10000)
                    if TweetGatherer.Keys.data.fileTrackerData['fileNum'] < fileNum:
                        TweetGatherer.Keys.data.fileTrackerData['fileNum'] += 1
                        TweetGatherer.Keys.dataLoader.update_file_tracker_data(
                            TweetGatherer.Keys.data.fileTrackerData['tweetNum'],
                            TweetGatherer.Keys.data.fileTrackerData['fileNum'])
                    print TweetGatherer.Keys.data.fileTrackerData
                    fileString = 'TrumpData' + str(TweetGatherer.Keys.data.fileTrackerData['fileNum']) + '.txt'
                    saveFile = open(fileString, 'a')
                    saveFile.write(str_data)
                    saveFile.close()
                    TweetGatherer.Keys.data.fileTrackerData['tweetNum'] += 1
                    TweetGatherer.Keys.dataLoader.update_file_tracker_data(
                        TweetGatherer.Keys.data.fileTrackerData['tweetNum'],
                        TweetGatherer.Keys.data.fileTrackerData['fileNum'])
                    return True

                except BaseException, e:
                    print 'failed OnData: ', str(e)
                    time.sleep(5)
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
        time.sleep(30)


# Setting Authentication Keys for API
auth = OAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth)
auth.set_access_token(accessToken, accessSecret)
twitterStream = Stream(auth, Listener())

# Gathering tweets with keyword Trump
twitterStream.filter(track=["Trump, suck"])
print "hello"


# ---------gathering information on users via username ------------ #
# users = [818568080536178688, 0]
# username = api.lookup_users(users)
# print username

# user_data = api.get_user('DylantheOstrich')
# print 'Followers: ' + str(user_data.followers_count)
# print 'Tweets: ' + str(user_data.statuses_count)
# print 'Favourites: ' + str(user_data.favourites_count)
# print 'Friends: ' + str(user_data.friends_count)
# print 'Appears on ' + str(user_data.listed_count) + ' lists'
# 818568080536178688 DYLANS IDa
