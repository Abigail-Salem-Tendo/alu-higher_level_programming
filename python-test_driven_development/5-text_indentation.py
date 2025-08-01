#!/usr/bin/python3
"""
This module contains the function text_indentation.
It prints text with 2 new lines after each '.', '?' or ':'.
"""


def text_indentation(text):
    """
    Prints text with 2 newlines after '.', '?', or ':' characters.

    Args:
        text: The input text string

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    new_text = ""
    for char in text:
        new_text += char
        if char in chars:
            new_text += "\n\n"

    lines = new_text.split('\n')
    for line in lines:
        stripped = line.strip()
        if stripped:
            print(stripped)
