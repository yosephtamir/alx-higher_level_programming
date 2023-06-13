#!/usr/bin/python3
"""
This module is used to print a new line
"""


def read_file(filename=""):
    """
    This function is used to open a file and print it to std
    """

    with open(filename, "r", encoding="utf-8") as e:
        for i in e:
            print(i, end="")
