#!/usr/bin/python3
"""this fetches  https://alu-intranet.hbtn.io/status"""


import urllib.request

url = "https://alu-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
except Exception as e:
    print("Error:", e)

