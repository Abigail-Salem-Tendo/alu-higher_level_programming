#!/usr/bin/python3
"""
Uses GitHub API to display the user's id
"""


import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
