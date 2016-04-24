from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Marker(models.Model):
	# most feilds are charfields (strings):
	# https://docs.djangoproject.com/en/1.9/ref/models/fields/#charfield
	# that way we can plug them directly into the javascript template
	latitude = models.CharField(max_length=100)
	longitude = models.CharField(max_length=100)
	longTitle = models.CharField(max_length=300)
	shortTitle = models.CharField(max_length=50)
	redditLink = models.CharField(max_length=200)
	imageLink = models.CharField(max_length=300)
	uniqueID = models.CharField(max_length=50) # this is how we'll check for duplicates
	utxTimestamp = models.FloatField() 
	intScore = models.IntegerField()
	
	# Timestamp doesn't need to go into the template, so it's the regular one:
	time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.shortTitle + "(" + self.latitude + ", " + self.longitude + ")"

