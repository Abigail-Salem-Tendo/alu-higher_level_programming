#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_use
with a letter.
"""


import requests
import sys

if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

url = "http://0.0.0.0:5000/search_user"
data = {'q': q}

try:
    response = requests.post(url, data=data)
    json_data = response.json()

    if json_data:
        print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
