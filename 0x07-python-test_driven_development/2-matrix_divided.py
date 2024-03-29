#!/usr/bin/python3
"""Divises all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""
    new_matrix = []

    # Check if div is a valid value
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        # check if element is a list
        if isinstance(i, list):
            row_length = len(matrix[0])

            # check if rows in matrix are equal
            if len(i) != row_length:
                raise TypeError("Each row of the matrix must "
                                "have the same size")

            row = []
            for j in i:
                if not isinstance(j, int) and not isinstance(j, float):
                    raise TypeError("matrix must be a matrix "
                                    "(list of lists) of integers/floats")
                row.append(round((j / div), 2))
            new_matrix.append(row)
        else:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")

    return new_matrix
