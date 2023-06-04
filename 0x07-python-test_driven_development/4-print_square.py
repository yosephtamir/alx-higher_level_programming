#!/usr/bin/python3
"""
This module is used to print a square of # as per the size
"""


def print_square(size):
    """
    print_square: is used to print a square of #
    args:
        @size: is the size of the # to be printed as square
    return: no return value
    """

    if not (isinstance(size, int) or isinstance(size, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        if (size < 1 and size > 0):
            raise TypeError("size must be an integer")
        size = int(size)

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
