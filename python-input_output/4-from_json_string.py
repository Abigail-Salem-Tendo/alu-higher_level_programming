#!/usr/bin/python3
"""
This module has a function that returns an
object (ds) represented by a json string
"""


import json


def from_json_string(my_str):
    """
    This function returns the object
    represented
    """
    return json.loads(my_str)
