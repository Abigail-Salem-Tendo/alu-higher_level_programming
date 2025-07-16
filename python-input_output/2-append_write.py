#!/usr/bin/python3
"""
This module appends to a file
"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
