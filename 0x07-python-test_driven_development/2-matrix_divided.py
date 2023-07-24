#!/usr/bin/python3

"""Module have matrix div function"""


def matrix_divided(matrix, div):
    """
        Return the matrix divided by the div
        matrix: [[int, int], [int, int]]
        div: not zero
    """
    if not isinstance(matrix, list) or not matrix:
        error()
    if not isinstance(matrix[0], list):
        error()
    number_elements = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            error()
        if len(row) != number_elements:
            raise TypeError("Each row of the matrix must have the same size")

        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                error()
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round((num / div), 2) for num in row_1] for row_1 in matrix]
    return new


def error():
    """error 1"""
    raise TypeError("matrix must be a matrix (list of lists) of "
                    "integers/floats")
