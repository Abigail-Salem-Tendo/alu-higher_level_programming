#!/usr/bin/python3
"""
Rectangle that inherits from
BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    REctangle inheriting from BaseGeometry class
    """

    def __init__(self, width, height):
        """
        Initailize rectangle with validated
        width and height
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
