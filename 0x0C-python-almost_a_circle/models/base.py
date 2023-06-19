#!/usr/bin/python3
"""
This is the base of all other class of this project
"""


class Base:
    """
    This is the base class
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        This is an instantaniation
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
