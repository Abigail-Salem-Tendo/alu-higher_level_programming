#!/usr/bin/python3
"""
This module deinfes class MyList that inherits from list.
"""


class MyList(list):
    """
    This is a subclass of list with a methond that prints
    the list in sorted order
    """

    def print_sorted(self):
        """Prints the list in sorted ascending order.
        """
        print(sorted(self))
