# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
	name = models.CharField(max_length=100)
	acronym = models.CharField(max_length=3)

def __unicode__(self):
	return u'%s or %s' % (self.name, self.acronym)

class DailyWeather(models.Model):
	day = models.DateField()
	temperature = models.IntegerField()
	city = models.ForeignKey('City')

def __unicode__(self):
	return u'Weather forecast for tomorrow in %s:\n %s º' % (self.city.name, self.s)
