import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
import string
import re
import json
import urllib2
import praw
import sys
from .models import Marker




def index(request):
	marker_list = Marker.objects.all()
	context = {'marker_list': marker_list}
	return render(request, 'script.js', context)
	
@staff_member_required
def runbot(request):
	
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
	
	
	
	
	print >>sys.stderr, 'Running bot!'
	
	user_agent = ("WanderMap by /u/CSCI3308Project")
	r = praw.Reddit(user_agent = user_agent)
	r.login('CSCI3308Project', 'buffs10')
	subreddit = r.get_subreddit("EarthPorn")
	
	for submission in subreddit.get_top(limit = 500):  #, period = 'day'): # Get the top 25 hot posts PERIOD equals previous 24 hours
		
		value = submission.title
		print >>sys.stderr, 'Looking at {0}....'.format(submission.id)
		
		# geoLocate also returns a status. "ZERO_RESULTS" means we can't imply a lat,lng for this place
		# "BAD_STRING" means a blank string was passed
		# "OK" means we found some lat,lng for the string, which usually is a good guess!
		longTitle = value
		shortTitle = getShortTitle(value)
		status, lat, lng = geoLocate(shortTitle)
		
		# grab any markers with the unique ID we grabbed
		check = Marker.objects.filter(uniqueID=submission.id).first()
		
		# debug:
		print >>sys.stderr, 'Status: {0}, {1}'.format(status,check)
		
		# If we actually get something, then this IF statement will fail (already have this marker)
		# If not, then we don't have this marker in our database, so we're OK to add it
		# This means we 'should' be able to run this bot whenever we want and it won't spam the database
		if check == None and status == "OK":
			marker = Marker()
			marker.latitude = lat
			marker.longitude = lng
			marker.longTitle = value
			marker.shortTitle = shortTitle
			marker.redditLink = submission.permalink
			marker.imageLink = submission.url
			marker.utxTimestamp = submission.created
			marker.intScore = submission.score
			marker.uniqueID = submission.id
			marker.save()
	print >>sys.stderr, 'All done.'
	return render(request, 'script.js')


