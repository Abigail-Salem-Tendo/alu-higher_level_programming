#!/usr/bin/python3
"""
This module contains a function
that writes an object to a text file
using a json representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using json
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
