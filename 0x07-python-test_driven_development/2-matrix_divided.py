#!/usr/bin/python3
"""
This Module is used to devide a matrix
"""


def matrix_divided(matrix, div):
    """
    This function is used to devide the matrix passed to this module
    by the division number passed to this module
    """

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    outerList = []
    for inner in matrix:
        if not isinstance(inner, list):
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        innerMatrix = []
        for inMost in inner:
            if not (isinstance(inMost, int) or isinstance(inMost, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")
            inMost = round(inMost / div, 2)
            innerMatrix.append(inMost)
        if len(innerMatrix) != 0:
            outerList.append(innerMatrix)
    return outerList
