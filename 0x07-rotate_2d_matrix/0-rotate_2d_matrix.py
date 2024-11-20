#!/usr/bin/python3
import math


def rotate_2d_matrix(matrix):
    """
    a function that rotates a matrix of n * n type
    """
    # transpose matrix
    matrix_lenght = len(matrix)
    for i in range(math.ceil(matrix_lenght / 2)):
        for j in range(i, matrix_lenght):
            x = matrix[i][j]
            y = matrix[j][i]
            matrix[j][i] = x
            matrix[i][j] = y

    # reverse rows
    for row in range(len(matrix)):
        for element in range(math.ceil(len(matrix[row]) / 2) - 1):
            first = matrix[row][element]
            last = matrix[row][len(matrix[row]) - 1 - element]
            matrix[row][element] = last
            matrix[row][len(matrix[row]) - 1 - element] = first
