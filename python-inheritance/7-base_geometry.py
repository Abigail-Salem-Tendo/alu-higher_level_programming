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

    def integer_validator(self, name, value):
        """
        Validates the value os positive integer
        raises two errors typeerror and valueerror
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
