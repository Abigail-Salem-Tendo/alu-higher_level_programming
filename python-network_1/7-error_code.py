#!/usr/bin/python3
"""
Takes in a url, sends a request to the url and
displays the body of the response.
"""


import requests
import sys

url = sys.argv[1]
response = requests.get(url)

if response.status_code >= 400:
    print("Error code: {}".format(response.status_code))
else:
    print(response.text)
