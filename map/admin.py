from django.contrib import admin

from .models import Marker
import praw
import re
import string
import urllib
import json
from geopy.geocoders import Nominatim

class MarkerAdmin(admin.ModelAdmin):
	list_display = ['shortTitle', 'latitude', 'longitude']
	ordering = ['shortTitle']
	actions = [pull_top]

# Register your models here.
admin.site.register(Marker, MarkerAdmin)
