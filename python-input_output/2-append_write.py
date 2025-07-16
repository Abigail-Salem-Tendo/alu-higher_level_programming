#!/usr/bin/python3
"""
This module appends to a file
"""


def append_write(filename="", text=""):
    """Append to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
