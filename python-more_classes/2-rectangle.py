#!/usr/bin/python3
"""This is a class that is based
off 1-rectangle but finds the area
and perimeter
"""


class Rectangle:
    """This class deines the methods and attributes
    Attributes: include width, height, and value
    """
    def __init__(self, width=0, height=0):
        """Initialsing the class"""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """REtrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Validating the value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Validating the height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
