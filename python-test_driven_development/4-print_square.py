#!/usr/bin/python3
"""
This module defines a function that prints a square using # characters.
"""


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size: The size of the square (must be a non-negative integers)

    Raises:
        TypeError: If size is not and integer
        ValueError: If size is less than 0
    """

    if isinstance(size, float) and size < 0:
        raise TypeError ("size nust be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print('#' * size)
