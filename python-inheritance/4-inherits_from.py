#!/usr/bin/python3
"""
checks if an object inherits from
a specific class
"""


def inherits_from(obj, a_class):
    """
    Return true is obj is an instance of a subclass
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
