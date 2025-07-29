#!/usr/bin/python3
"""
Send a post request with an email and displays
the response body (utf-8)
"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
	url = sys.argv[1]
	value = {'email' : sys.argv[2]}

	data = urllib.parse.urlencode(value).encode('ascii')
	req = urllib.request.Request(url, data)

	with urllib.request.urlopen(url, data) as response:
    		body = response.read().decode('utf-8')
    		print(body)
