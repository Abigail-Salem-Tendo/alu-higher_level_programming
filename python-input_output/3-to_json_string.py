#!/usr/bin/python3
"""
This module contains a function that
returns the JSON representaion of
a string
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation
    of a string
    """
    return json.dumps(my_obj)
