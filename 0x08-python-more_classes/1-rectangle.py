#!/usr/bin/python3
"""
This the class Rectangle
"""


class Rectangle:
    """
    this is used to calculate parameters of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        this is the instantation of the class
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        this is used to return the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This is used to set the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        This is used to return the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        this is used to set the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
