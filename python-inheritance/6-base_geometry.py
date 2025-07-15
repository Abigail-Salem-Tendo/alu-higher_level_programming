#!/usr/bin/python3
"""
Defines a class BaseGeometry with an
unimplemented area method.
"""


class BaseGeometry:
    """
    BAseGeometry class with area method
    """

    def area(self):
        """
        Raises an exception indicated it
        has not been implemented
        """
        raise Exception("area() is not implemented")
