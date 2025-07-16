#!/usr/bin/python3
"""
This module has a function that
creates an object
from a json file
"""


import json


def load_from_json_file(filename):
    with open(filename, "w", encoding="utf-8") as f:
        return json.loads(f)
