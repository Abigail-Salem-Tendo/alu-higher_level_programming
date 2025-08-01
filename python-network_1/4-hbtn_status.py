#!/usr/bin/python3
"""fetches https://alu-intranet.hbtn.io/status"""


import requests

url = [
        'https://alu-intranet.hbtn.io/status',
        'http://0.0.0.0:5000/status'
]
response = requests.get(url)
text = response.text

print("Body response:")
print("\t- type:", type(text))
print("\t- content:", text)
