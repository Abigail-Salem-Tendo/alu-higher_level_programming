#!/usr/bin/python3
"""Checks if an objects is exactly
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    return true is obj is exactly and instance
    of a_class, else False
    """
    return type(obj) is a_class
