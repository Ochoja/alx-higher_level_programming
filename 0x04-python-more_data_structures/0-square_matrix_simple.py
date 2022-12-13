#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Function computes the square value of a matrix
    """
    new_matrix = []
    for i in matrix:
        new_matrix.push([])
        for j in matrix[i]:
            new_matrix[i].push(matrix[i][j] ** 2)

    return new_matrix
