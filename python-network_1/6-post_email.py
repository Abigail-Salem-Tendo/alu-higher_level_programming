#!/usr/bin/python3
"""
Sends a POSt request with an email and
prints the response body
"""


import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

payload = {'email': email}
response = requests.post(url, data=payload)
print(response.text)
