#!/usr/bin/python3
"""
This module divides all elements of a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix (_type_): _list of lists of integers or floats_
        div (_type_): a _a number (integer or float)_

    Raises:
        TypeError: if div is not an integer_
        ZeroDivisionError: if div is 0_
        TypeError: if all the lists in matrix are not of same length_
        TypeError: if matrix is not a list of lists_
        TypeError: if any list contains a value diff frim an integer
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    message = "matrix must be a matrix (list of lists) of integers/floats"
    m = matrix
    if not isinstance(m, list) or not all([isinstance(x, list) for x in m]):
        raise TypeError(message)

    if len(matrix) == 0:
        raise TypeError(message)

    length = len(matrix[0])

    if not all([len(x) == length for x in matrix]):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for arr in matrix:
        new_list = []
        for num in arr:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(message)
            new_list.append(round((num / div), 2))
        new_matrix.append(new_list)
    return new_matrix
