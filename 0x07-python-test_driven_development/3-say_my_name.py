#!/usr/bin/python3
"""
This module is used to say a name passed as an argument
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: is used to print a name passed as an argument
    args:
        first_name: is the str passed to this function
        last_name: is the optional argument passed to this function
    return: nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
