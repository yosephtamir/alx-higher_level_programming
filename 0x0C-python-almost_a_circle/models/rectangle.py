#!/usr/bin/python3
"""
This is used to define a Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a Rectangle class which inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantation
        """
        super().__init__(id)

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
        This is used to return the value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This is used to set the value
        """
        self.checker(value, 'width')

        self.__width = value

    @property
    def height(self):
        """
        This is used to return the value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is used to set the value
        """
        self.checker(value, 'height')

        self.__height = value

    @property
    def x(self):
        """
        This is used to return the value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This is used to set the value
        """
        self.checker(value, 'x')

        self.__x = value

    @property
    def y(self):
        """
        This is used to return the value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This is used to return the value
        """
        self.checker(value, 'y')

        self.__y = value

    def checker(self, value, fromWhere):
        """
        This method is used to check the value
        """

        if not isinstance(value, int):
            raise TypeError(f"{fromWhere} must be an integer")

        if value <= 0:
            if fromWhere in ('width', 'height'):
                raise ValueError(f"{fromWhere} must be > 0")

        if value < 0:
            if fromWhere in ('x', 'y'):
                raise ValueError(f"{fromWhere} must be >= 0")

    def area(self):
        """
        This is a method used to calculate an areaof a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        This is used to print a rectangular # based on the rectangle
        """
        if self.__width != 0 and self.__height != 0:
            for k in range(self.__y):
                print("")
            for i in range(self.__height):
                for lim in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print("")

    def __str__(self):
        """
        This is str method which returns [Rectangle]
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        This method is used to update the order of args
        """
        arg = len(args)
        kwarg = len(kwargs)
        newOrder = ['id', 'width', 'height', 'x', 'y']

        if arg > 5:
            arg = 5

        if arg > 0:
            for i in range(arg):
                setattr(self, newOrder[i], args[i])
        elif kwarg > 0:
            for j, k in kwargs.items():
                if j in newOrder:
                    setattr(self, j, k)

    def to_dictionary(self):
        """
        This method is used to add to dictionary
        """
        return {'x': self.x, 'y': self.y,
                'id': self.id, 'height': self.height, 'width': self.width}
