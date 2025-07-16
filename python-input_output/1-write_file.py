#!/usr/bin/python3
"""
This module writes a string to a text file
and returns the number of characters
"""


def write_file(filename="", text=""):
    """Write in a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
