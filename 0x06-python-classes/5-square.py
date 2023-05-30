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

    @property
    def size(self):
        """
        Used to return the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is used to set the value of the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        this method is used to return the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        This method is used to print # as a square
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
