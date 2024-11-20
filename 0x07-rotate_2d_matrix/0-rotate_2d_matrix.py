#!/usr/bin/python3
"""
this modul contains one function to rotate a n * n matrix
"""


def ceil(number):
    """
    a local implementation of the ceil function
    since im not allowed to import any module -_-
    """
    if type(number) is float:
        return int(number + 1)
    else:
        return number


def rotate_2d_matrix(matrix) -> None:
    """
    a function that rotates a matrix of n * n type
    """
    # transpose matrix
    matrix_lenght: int = len(matrix)
    for i in range(ceil(matrix_lenght / 2)):
        for j in range(i, matrix_lenght):
            x: int = matrix[i][j]
            y: int = matrix[j][i]
            matrix[j][i] = x
            matrix[i][j] = y

    # reverse rows
    for row in range(len(matrix)):
        for element in range(ceil(len(matrix[row]) / 2) - 1):
            first: int = matrix[row][element]
            last: int = matrix[row][len(matrix[row]) - 1 - element]
            matrix[row][element] = last
            matrix[row][len(matrix[row]) - 1 - element] = first
