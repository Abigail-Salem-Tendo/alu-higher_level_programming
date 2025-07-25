#!/usr/bin/python3
"""Sends request to url and handles errors gracefully"""


import requests
import sys

url = sys.argc[1]
response = requests.get(url)

if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(response.text)
