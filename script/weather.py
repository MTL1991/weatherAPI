#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import sys
import urllib, json
import argparse

serverUrl = "http://weatherapimanuel.herokuapp.com/api/"

def return_temperature(url):
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	date = 'tomorrow'
	if data:
		for key,value in data.items():
		    if(str(key)=='city'):
		    	city = value
		    if(str(key)=='temp'):
		    	temperature = value
		    if(str(key)=='date'):
		    	date=value
		    if(str(key)=='error'):
		    	print value
		    	return
	else:
		print "No info"
	print "Weather forecast for "+date+" in " +str(city) +"\nTemperature:"+ str(temperature)

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--city", help="Select City")
parser.add_argument("-d", "--day", help="Specific day in dd/mm/yyyy")

args = parser.parse_args()

if args.day:
    if args.city:
    	url = serverUrl+args.city+"/"+args.day
    	return_temperature(url)
    else:
    	print "Where do you want to know the temperature? Please add a city"
elif args.city:
	url = serverUrl+args.city+"/"
	return_temperature(url)

