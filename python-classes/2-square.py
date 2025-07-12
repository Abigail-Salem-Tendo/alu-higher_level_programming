#!/usr/bin/python3
"""
This module deifnes a Square class with size validation
"""


class Square:
    """A class to represent a square with a private size attribute"""
    def size(self, size=0):
        """Initializes raises two errors TypeError and ValueError"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
