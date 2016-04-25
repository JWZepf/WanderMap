#!/usr/bin/python
'''
import praw

user_agent = ("WanderMap Bot 0.1")  # Sets name of User Agent that we will use

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("earthporn") # We are looking at /r/earthporn

array = []
for submission in subreddit.get_hot(limit = 25): # Get the top 25 hot posts
    array.append(submission.title)

    print ("Title: ", submission.title)
    print ("Text: ", submission.selftext)
    print ("Score: ", submission.score)
    print ("---------------------------------\n")

print (array[5])
'''
import os
import time
import re
import string
import time
import wget
#nltk.data.path.append('path_to_nltk_data')
#import geograpy

import praw
from array import *

user_agent = ("WanderMap by /u/CSCI3308Project")

r = praw.Reddit(user_agent = user_agent)

r.login('CSCI3308Project', 'buffs10')

subreddit = r.get_subreddit("EarthPorn")

identifiers = ['i.imgur.com', 'jpg', 'png']

while True:
	for submission in subreddit.get_hot(limit=50):
		value = submission.title
		value1 = ''.join(value)
		output = re.sub("[\(\[].*?[\)\]]", "", value1, flags=re.MULTILINE)
		output.strip()
		url_text = submission.url
		domain = any(string in url_text for string in identifiers)
		# from geopy.geocoders import Nominatim
		# geolocator = Nominatim()
		# location = geolocator.geocode(output)
		# places = geograpy.get_place_context(output = output)
		# print(places)
		# print(location.latitude, location.longitude)#


        print (domain)
        print(location.address)
		print(output)
		print '[LOG] Getting url:  ' + url_text
	time.sleep(30)
