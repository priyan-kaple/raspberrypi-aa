#!/usr/bin/env python

import requests

# Making a simple request
r = requests.get('http://google.com')
print r.text
dir(r)

# Passing parameters to the request
#searchTerms = {'q' : 'raspberryPi'} 
#r = requests.get('http://google.com/search', params=searchTerms)
#print r.text
#print r.response

