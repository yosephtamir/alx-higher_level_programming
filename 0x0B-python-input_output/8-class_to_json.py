#!/usr/bin/python3
"""
a function that returns the dictionary description with sample
data structure
"""


def class_to_json(obj):
    """
    simply return the dict
    """
    return (obj.__dict__)
