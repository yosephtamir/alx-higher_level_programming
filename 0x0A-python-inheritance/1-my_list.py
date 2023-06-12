#!/usr/bin/python3
"""
This is a class that inherests from list
"""


class MyList(list):
    """
    This is simply used to pass the argument
    """
    def __init__(self):
        """
        This is used to pass to the list init
        """
        super().__init__()

    def print_sorted(self):
        """
        This function is used to print a sorted list
        """
        print(sorted(self))
