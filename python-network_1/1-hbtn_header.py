#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""


import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

with urllib.request.urlopen(url) as response:
    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)
