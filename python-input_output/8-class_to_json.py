#!/usr/bin/python3
"""
This module has a function taht returns
a dictionary description of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary destination
    for json serialisation of a simple object
    """
    return obj.__dict__
