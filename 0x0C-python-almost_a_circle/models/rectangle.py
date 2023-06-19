#!/usr/bin/python3
"""
This is a rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a rectangle class which inherits from the base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is an instantaniation point
        """
        super().__init__(id)
        """
        These four function is used to check whether it is allowable value
        """

        self.checker(width, 'width')
        self.checker(height, 'height')
        self.checker(x, 'x')
        self.checker(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Used to return the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Used to set the value of width
        """
        self.checker(value, 'width')
        self.__width = value

    @property
    def height(self):
        """
        Used to return the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Used to set the value of height
        """
        self.checker(value, 'height')
        self.__height = value

    @property
    def x(self):
        """
        Used to return the value of x
        """
        return self.x

    @x.setter
    def x(self, value):
        """
        Used to set the value of x
        """
        self.checker(value, 'x')
        self.x = value

    @property
    def y(self):
        """
        used to return the value of y
        """
        return self.y

    @y.setter
    def y(self, value):
        """
        Used to set the value of y
        """
        self.checker(value, 'y')
        self.__y = value

    def checker(self, value, place):
        """
        This is used to check all variables
        """
        if not isinstance(value, int):
            raise TypeError(f"{place} must be an integer")
        if value <= 0:
            if place in ('width', 'height'):
                raise ValueError(f"{place} must be > 0")
        if value < 0:
            if place in ('x', 'y'):
                raise ValueError(f"{place} must be >= 0")
