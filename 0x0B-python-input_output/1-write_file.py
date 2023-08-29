#!/usr/bin/python3
"""
This module is used to insert a character to file and returns
the number of character
"""


def write_file(filename="", text=""):
    """
    this is used to write a text to a filename
    """
    with open(filename, 'w', encoding="utf-8") as e:
        return e.write(text)
