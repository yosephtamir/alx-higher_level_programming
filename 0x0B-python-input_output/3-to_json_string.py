#!/usr/bin/python3
"""
This is used to return json representation
"""
from json import dumps


def to_json_string(my_obj):
    """
    This returns json representation
    """
    return (dumps(my_obj))
