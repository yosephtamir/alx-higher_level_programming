#!/usr/bin/python3
"""
This function appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    this method is to add a string to the last line
    """

    with open(filename, 'a', encoding="utf-8") as e:
        return e.write(text)
