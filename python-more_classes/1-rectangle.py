#!/usr/bin/python3
"""
This class defines a rectangle based on
width and height
"""


class Rectangle:
    """Private instance attribute width"""

    def __init__(self, width=0, height=0):
        """Initialze the rectangle with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
