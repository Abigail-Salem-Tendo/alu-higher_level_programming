#!/usr/bin/python3
"""This module defines Square class with provate size and area calculation."""

class Square:
    """A class that defines a square by its size"""
    def __init__(self, size=0):
        """Initializes a square instance
        raise two errors
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2
