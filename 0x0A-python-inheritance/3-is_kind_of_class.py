#!/usr/bin/python3
"""
This module uses inheritance to return the required value
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns true if it is inheritance of the class
    otherwise Fals
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
