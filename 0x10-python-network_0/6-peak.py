#!/usr/bin/python3
"""A function used to find a maximum number"""


def find_peak(list_of_integers):
    """This method is used to find a maximum number from a given int list"""
    if(isinstance(list_of_integers, list)):
        try:
            return max(list_of_integers)
        except Exception:
            return
