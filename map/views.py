import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

from django.contrib.admin.views.decorators import staff_member_required
import praw
import re
import string
import urllib
import json
from geopy.geocoders import Nominatim
from .models import Marker

def index(request):
	marker_list = Marker.objects.all()[:5]
	context = {'marker_list': marker_list}
	return render(request, 'script.js', context)

@staff_member_required
def bot(request):
	user_agent = ("WanderMap 0.1")  # Sets name of User Agent that we will use
	r = praw.Reddit(user_agent = user_agent)
	subreddit = r.get_subreddit("earthporn") # We are looking at /r/earthporn
	for submission in subreddit.get_top(limit = 5,period = 'day'): # Get the top 25 hot posts PERIOD equals previous 24 hours
		value = submission.title
		url_text = submission.url
		marker = Marker()
		marker.latitude = 'none'
		marker.longitude = 'none'
		marker.longTitle = value
		marker.shortTitle = 'none'
		marker.redditLink = 'none'
		marker.imageLink = url_text
		marker.save()
	return render(request, 'script.js')


def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)
	
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
    
def loggedin(request):
    return render_to_response('loggedin.html', 
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
    
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    else:
        form = UserCreationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')
