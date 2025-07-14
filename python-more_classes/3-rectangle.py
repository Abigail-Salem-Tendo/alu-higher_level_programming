#!/usr/bin/python3
"""This module defines a rectangle with widdth and height
validated and has methos for area, perimeter, and string
representation.
"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional
        width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height with validation"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height wiwth validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Return a string representation of the
        rectangle using '#'.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for i in range(self.height):
            rectangle += "#" * self.width
            if i != self.height - 1:
                rectangle += "\n"
        return rectangle
