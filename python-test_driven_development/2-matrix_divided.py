#!/usr/bin/python3
"""
This module provides a function to divide all elememts of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix: A list of lists containing integers or floats.
        div: A number (int or float) by which to divide the elements.

    Returns:
        A new matrix with all elements divided by div rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of listss of integers/floats,
            or if rows are not the same size,
            or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list)for row in matrix
    ):
        raise TypeError(
                "matrix must be matrix (list of lists) of integers/floats"
        )
    row_lengths = {len(row) for row in matrix}
    if len(row_lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("dividion by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
