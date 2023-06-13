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

    def to_json(self, attrs=None):
        """
        that recieces a dict rep
        simply returns a dict
        """
        if attrs is None:
            return (self.__dict__)
        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})

    def reload_from_json(self, json):
        """
        repl all atr
        """
        self.__dict__.update(json)
