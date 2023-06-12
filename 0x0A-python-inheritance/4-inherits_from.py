#!/usr/bin/python3
"""
a module used to return a subclass
"""


def inherits_from(obj, a_class):
    """
    a method used to return true if it is a subclass
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
