#!/usr/bin/python3
"""
This function modifies the BaseGeometery class
"""


class BaseGeometry:
    """
    This is on progress
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This is used to validate the integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
