#!/usr/bin/python3
"""
Send a post request with an email and displays
the response body (utf-8)
"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('ascii')

with urllib.request.urlopen(url, data) as response:
    body = response.read().decode('utf-8')
    print(body)
