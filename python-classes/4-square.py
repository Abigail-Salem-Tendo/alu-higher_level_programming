#!/usr/bin/python3
"""
This module defines a Square class with a private size,
a property getter and a setter, and area calculation.
"""


class Square:
    """
    Represents a square with a private size attribute.
    """

    def __init__(self, size=0):
        """Initializes a square instance with optional size.
        Raises:
        TypeError: If size is not an integer
        Valueerror: If size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes and returns the area of a square
        """
        return self.__size ** 2
