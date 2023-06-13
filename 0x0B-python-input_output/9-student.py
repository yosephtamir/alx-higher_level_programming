#!/usr/bin/python3
"""
a class Student that defines a student
"""


class Student:
    """
    a class Student that defines a student by following
    """
    def __init__(self, first_name, last_name, age):
        """
        instantation or main entery of attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        simply returns a dict
        """
        return (self.__dict__)
