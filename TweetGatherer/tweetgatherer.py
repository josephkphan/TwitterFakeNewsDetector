import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import key
import time
import json

# ------------Keys for API---------- #
consumerKey = key.consumerKey
consumerSecret = key.consumerSecret
accessToken = key.accessToken
accessSecret = key.accessSecret


# Creating Listener class that will gather data from API
class Listener(StreamListener):
    # Authentication worked and getting data

    def on_data(self, str_data):
        try:
            # data from on_data initially comes in as string. Converts to json
            # print str_data
            data = json.loads(str_data)

            # Checking if keys exist in data
            if 'id' in data and 'text' in data and 'user' in data:
                try:
                    if key.tweetNum%1000 ==0:
                        key.tweetNum +=1
                        time.sleep(300)
                    fileNum = int(key.tweetNum/10000)
                    if key.curFileNum < fileNum:
                        key.curFileNum = fileNum
                        
                        return True
                    fileString = 'TrumpData'+ str(key.curFileNum) + '.txt' 
                    saveFile = open(fileString, 'a')
                    saveFile.write(str_data)
                    saveFile.close()
                    key.tweetNum+=1
                    return True

                except BaseException, e:
                    print 'failed OnData: ', str(e)
                    time.sleep(5)

            else:
                # Data does not exist. Ignore this case
                print "information does not exist"

            return True

        # Could happen with bad internet... etc other errors
        except BaseException, e:
            print 'failed on_data,', str(e)
            time.sleep(5)

        def print_data():
            print data['id']
            print data['text']
            print data['user']['name']
            print data['user']['screen_name']

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
twitterStream.filter(track=["Trump"])


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
