#!/usr/bin/python3
"""
This module defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (which are casted to integers).

    Args:
        a: An integer or float
        b: An integer or float, default is 98.

    Returns:
        The integer addition of a and b.

    Raises:
        TypeError: If a or b are nor integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
