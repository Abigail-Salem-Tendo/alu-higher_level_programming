#!/usr/bin/python3
"""
This module defines a rectangle
methods for area, perimeter, and
special string
"""


class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initializes the rectacngle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height with validation"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area"""
        return self.width * self.height

    def perimeter(self):
        """return the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """return string representation"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """return the strng that recreates the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when the rectangle is deleted"""
        print("Bye rectangle...")
