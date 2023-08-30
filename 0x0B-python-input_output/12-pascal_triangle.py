#!/usr/bin/python3
'''
This script returns a list of list of a pascal's triangle
'''
from math import factorial


def pascal_triangle(n):
    '''
    This is the function to return the list
    '''
    outerList = []
    for i in range(n):
        innerList = []
        for j in range(i + 1):
            innerList.append(factorial(i) // (factorial(i - j) * factorial(j)))
        outerList.append(innerList)
    return outerList
