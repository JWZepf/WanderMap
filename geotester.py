#!/usr/bin/python

import os
import sys
import time
import re
import string
import time
import json
import urllib2
import praw

def geoLocate(inputstr):
	inputstr = inputstr.replace(" ", "+") # spaces to pluses
	lat = None
	lng = None
	if not inputstr.strip():
		return ("BAD_STRING", lat, lng)
	
	# from http://stackoverflow.com/questions/13921910/python-urllib2-receive-json-response-from-url
	url = "https://maps.googleapis.com/maps/api/geocode/json?"
	url +="address={0}&key=AIzaSyDV4SQ_Dy4Az1C2f4XCL2H-Exe-bUovmJ8".format(inputstr)

	r = urllib2.urlopen(url)
	data = json.load(r)
	status = data['status']
	if status == "OK":
		lat = data['results'][0]['geometry']['location']['lat']
		lng = data['results'][0]['geometry']['location']['lng']
	return (status, lat, lng)

def getShortTitle(instring):
	reslist = re.findall(r"\[\S*\]|([A-Z][A-Za-z]+)", instring)
	return string.join(reslist," ")

def testGeoLocate(instring):
	print('Geolocating:')
	print instring
	result = getShortTitle(instring)
	print('Search string:')
	print result
	status, lat, lng = geoLocate(result)
	print('Results:')
	print status
	if status == "OK":
		print lat, lng
		print "Geolocating successful."
	else:
		print "Geolocating failed."
	

user_agent = ("WanderMap by /u/CSCI3308Project")
r = praw.Reddit(user_agent = user_agent)
r.login('CSCI3308Project', 'buffs10')
subreddit = r.get_subreddit("EarthPorn")
identifiers = ['i.imgur.com', 'jpg', 'png']

while True:
	for submission in subreddit.get_hot(limit=5):
		value = submission.title
		value1 = ''.join(value)
		output = re.sub("[\(\[].*?[\)\]]", "", value1, flags=re.MULTILINE)
		output.strip()
		
		longTitle = value
		shortTitle = getShortTitle(output)
		status, lat, lng = geoLocate(shortTitle)
		
		imageLink = submission.url
		print '[LOG] Short Title: ' + shortTitle
		print '------Status: ' + status
		if status == "OK":
			print '------Unique ID: {0}'.format(submission.id)
			print '------Created (Unix Timestamp): {0}'.format(submission.created)
			print '------Coordinates: {0}, {1}'.format(lat, lng)
			print '------Score: {0}'.format(submission.score)
		time.sleep(1)
	time.sleep(300)

