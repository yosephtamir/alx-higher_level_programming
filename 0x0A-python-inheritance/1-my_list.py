#!/usr/bin/python3
"""
This is a class that inherests from list
"""


class MyList(list):
    """
    This is simply used to pass the argument
    """
    def print_sorted(self):
        """
        This function is used to print a sorted list
        """
        print(sorted(self))
