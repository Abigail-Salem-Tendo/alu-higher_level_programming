#!/usr/bin/python3
"""
Square class that inherits from
REctangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class based on Rectangle"""

    def __init__(self, size):
        """initializes the square wiwth size"""
        self.integer_validator("size", size)
        self.__size = size
        duper().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
