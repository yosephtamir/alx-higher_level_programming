#!/usr/bin/python3
"""
This module is used to add two given integers
"""


def add_integer(a, b=98):
    """
    This function is used to add two integers
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return a + b
