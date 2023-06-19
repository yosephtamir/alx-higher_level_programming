#!/usr/bin/python3
"""
This is a square a class like rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantation
        """
        super().__init__(size, size, x, y, id)

    def __str___(self):
        """
        the string representation
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        This is used to return the value of width or height
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        This is used to set the value of width and height to size
        """
        self.width = value
        self.height = value

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
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
