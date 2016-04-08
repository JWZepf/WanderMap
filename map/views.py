import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Marker

def index(request):
	marker_list = Marker.objects.all()[:5]
	context = {'marker_list': marker_list}
	return render(request, 'script.js', context)
