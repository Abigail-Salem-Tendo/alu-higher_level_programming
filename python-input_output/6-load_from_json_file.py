#!/usr/bin/python3
"""
This module has a function that
creates an object
from a json file
"""


import json


def load_from_json_file(filename):
    """ loads from a json file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
