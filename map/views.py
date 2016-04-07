import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Marker

def index(request):
	'''
	post = {
		'lat': 39.2599775,
		'lng': -107.1715559,
		'title': 'Storm Clouds over Mount Sopris, Colorado. [OC][4354x2900]',
		'linkto': 'https://www.reddit.com/r/EarthPorn/comments/4c8g6z/storm_clouds_over_mount_sopris_colorado/',
		'shorttitle': 'Mount Sopris',
		'imgsrc': 'http://i.imgur.com/DQdWvz2.jpg'
	}
	return render(request, 'index.html', post)
	'''
	marker_list = Marker.objects.all()[:5]
	context = {'marker_list': marker_list}
	return render(request, 'index.html', context)
