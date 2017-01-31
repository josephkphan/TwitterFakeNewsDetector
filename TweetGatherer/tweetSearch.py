import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import data
import dataLoader

consumerKey = data.key['consumerKey']
consumerSecret = data.key['consumerSecret']
accessToken = data.key['accessToken']
accessSecret = data.key['accessSecret']

auth = OAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth)
auth.set_access_token(accessToken, accessSecret)

# Use csv Writer
# fileString = 'testing.txt'
# saveFile = open(fileString, 'a')
# saveFile.write(str_data)
# saveFile.close()
fileString = 'testing.txt'
saveFile = open(fileString, 'a')


def get_text(string):
    buffer = string.split("text=")
    text = buffer[1].split(", ")
    return text[0]


def get_followers_count(string):
    buffer = string.split("followers_count=")
    text = buffer[1].split(",")
    return text[0]


def get_list_count(string):
    buffer = string.split("listed_count=")
    text = buffer[1].split(",")
    return text[0]


def get_status_count(string):
    buffer = string.split("statuses_count=")
    text = buffer[1].split(",")
    return text[0]


def get_favorite_count(string):
    buffer = string.split("favourites_count=")
    text = buffer[1].split(",")
    return text[0]


def get_screen_name(string):
    buffer = string.split("screen_name=u'")
    text = buffer[1].split("',")
    return text[0]


def get_id(string):
    buffer = string.split(", id=")
    text = buffer[1].split(",")
    return text[0]


def get_friend_count(string):
    buffer = string.split("friends_count=")
    text = buffer[1].split(",")
    return text[0]


def get_retweet_count(string):
    buffer = string.split("retweet_count=")
    text = buffer[1].split(",")
    return text[0]


for tweet in tweepy.Cursor(api.search,
                           q="Trump, hillary",
                           since="2017-01-29",
                           until="2017-01-30",
                           lang="en").items(10000):
    # Write a row to the csv file/ I use encode utf-8
    # print tweet
    tweet_string = str(tweet)
    tweet_data = {}
    tweet_data['text'] = get_text(tweet_string)
    tweet_data['retweet_count'] = get_retweet_count(tweet_string)
    tweet_data['friends_count'] = get_friend_count(tweet_string)
    tweet_data['id_str'] = get_id(tweet_string)
    tweet_data['screen_name'] = get_screen_name(tweet_string)
    tweet_data['favorite_count'] = get_favorite_count(tweet_string)
    tweet_data['status_count'] = get_status_count(tweet_string)
    tweet_data['list_count'] = get_list_count(tweet_string)
    tweet_data['followers_count'] = get_followers_count(tweet_string)
    print tweet_data
    # saveFile.write(str(tweet))
    # saveFile.write('\n')
saveFile.close()
