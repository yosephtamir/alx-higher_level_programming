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
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
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

    def area(self):
        """
        this method is used to calculate the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This is used to calculate the parameter of the given rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        This is used to return the str rep
        """
        thestr = ""
        for i in range(self.__height):
            for j in range(self.__width):
                thestr += "#"
            if i < (self.__height - 1):
                thestr += '\n'
        return thestr
