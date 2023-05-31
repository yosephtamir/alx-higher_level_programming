#!/usr/bin/python3
"""
This is only used to define size
"""


class Square:
    """
    the same here
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        this is an init function
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in position if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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

    @property
    def position(self):
        """
        is used to return the value of the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        this method is used to return the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        This method is used to print # as a square
        """
        t = 0
        if self.__size == 0:
            print("\n", end="")
        else:
            for i in range(self.__size):
                if t == 0:
                    for z in range(self.__position[1]):
                        print("\n", end="")
                        t = 1
                s = 0
                for j in range(self.__size):
                    if s == 0:
                        for k in range(self.__position[0]):
                            print(" ", end="")
                        s = 1
                    print("#", end="")
                print("\n", end="")
