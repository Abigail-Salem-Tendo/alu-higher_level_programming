#!/usr/bin/python3
"""display the value of X-reques-Id in response header"""


import requests
import sys

if __name__ == "__main__":
	url = sys.argv[1]
	response = requests.get(url)
	print(response.headers.get("X-Request-Id"))
