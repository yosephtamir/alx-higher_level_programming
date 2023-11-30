#!/usr/bin/python3
"""A function used to find a maximum number"""


def find_peak(list_of_integers):
    """This method is used to find a maximum number from a given int list"""
    if(isinstance(list_of_integers, list)):
        try:
            num = list_of_integers[0]
        except Exception:
            return
        for i in list_of_integers:
            if i > num:
                num = i
    return num
