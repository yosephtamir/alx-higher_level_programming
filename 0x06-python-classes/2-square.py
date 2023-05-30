#!/usr/bin/python3
"""
This is only used to define size
"""


class Square:
    """
    the same here
    """
    def __init__(self, size=0):
        """
        this is an init function
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
