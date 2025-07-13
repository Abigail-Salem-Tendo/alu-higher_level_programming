#!/usr/bin/python3
"""
Defines a square class with size control,
area computation, and a method to print the square using "#"
"""


class Square:
    """
    A class to represent a square
    """

    def __init__(self, size=0):
        """Initialises the square with a given size.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with th3 # symbol
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
