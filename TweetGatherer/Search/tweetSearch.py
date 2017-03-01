import xlwt

import tweepy
from tweepy import OAuthHandler
import TweetGatherer.Keys.data

# ------------------ What you want to Find -------------------- #
# How to use Keywords:
# To input multiple phrases, Separate your strings with a commas
# ex: "Car" will find anything with
# ex: "Red Car" Will find anything with red and car in that exact format (i.e. This is a red car)
# ex: "Red, Car" Will find anything with Red and Car in the same sentence (i.e. I have a Car. I have a Red Apple)
# NOTE* Dates acn only go back 2 week in time!
keywords = "Trump, insult, Disabilities"
excelSheetName = "data.xls"
beginSearchDate = "2017-02-20"
endSearchDate = "2017-02-28"
# textFileName = "data.txt"

# ---------------- Access Keys ------------------#
consumerKey = TweetGatherer.Keys.data.key['consumerKey']
consumerSecret = TweetGatherer.Keys.data.key['consumerSecret']
accessToken = TweetGatherer.Keys.data.key['accessToken']
accessSecret = TweetGatherer.Keys.data.key['accessSecret']

auth = OAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth)
auth.set_access_token(accessToken, accessSecret)


# ------------ Tweet Extraction Functions ---------- #
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


def get_user_data(api, username):
    user_data = api.get_user(username)
    # print user_data
    return user_data


# ------------ Using Text File ------------- $
# Use csv Writer
# saveFile = open(fileString, 'a')
# saveFile.write(str_data)
# saveFile.close()
# fileString = 'testing.txt'
# saveFile = open(fileString, 'a')

# ----------- Using Excel Sheet ------------ $
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0, 0, "Tweet")
sheet1.write(0, 1, "Verified")
sheet1.write(0, 2, "Irrelevant")
sheet1.write(0, 3, "Username")
sheet1.write(0, 4, "userID")
sheet1.write(0, 5, "Tweet Length")
sheet1.write(0, 6, "Retweet Count")
sheet1.write(0, 7, "Friends Count")
sheet1.write(0, 8, "Followers Count")
sheet1.write(0, 9, "Status Count")
sheet1.write(0, 10, "Favorites Count")
sheet1.write(0, 11, "List Count")

# ------------ Iterating Through Tweets ------------ #
counter = 1
for tweet in tweepy.Cursor(api.search,
                           q= keywords,
                           since="2017-02-20",
                           until="2017-02-28",
                           lang="en").items(10000):
    tweet_string = str(tweet)
    # print "--------------------"
    # print tweet_string
    # print "--------------------"

    # Used to Skip "Reply Tweets"
    if tweet_string.find('RT') > 0:         # Returns index if found. Returns -1 if not found
        continue

    # Parsing through Tweet for data
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

    # Writing Data to Excel Sheet
    sheet1.write(counter, 0, tweet_data['text'])
    sheet1.write(counter, 3, tweet_data['screen_name'])
    sheet1.write(counter, 4, tweet_data['id_str'])
    sheet1.write(counter, 5, len(tweet_data['text'].split()))
    sheet1.write(counter, 6, tweet_data['retweet_count'])
    sheet1.write(counter, 7, tweet_data['friends_count'])
    sheet1.write(counter, 8, tweet_data['followers_count'])
    sheet1.write(counter, 9, tweet_data['status_count'])
    sheet1.write(counter, 10, tweet_data['favorite_count'])
    sheet1.write(counter, 11, tweet_data['list_count'])
    counter += 1

    # Writing to Text File
    # saveFile.write(str(tweet))
    # saveFile.write('\n')

book.save(excelSheetName)
# saveFile.close()
