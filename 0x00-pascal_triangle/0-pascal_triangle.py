#!/usr/bin/python3
"""
Module that defines a function to generate Pascal's triangle up to a given level.
"""


def try_get_elements_c1_c2(current_col: int, cached_row):
    """
    Calculate the sum of two elements in the previous row of Pascal's triangle.

    Args:
        current_col (int): The current column index in the row.
        cached_row (list): The previous row in the Pascal triangle.

    Returns:
        int: The sum of the two adjacent elements from the previous row.
    """
    position1 = current_col - 1
    position2 = current_col
    element1 = 0
    element2 = 0
    if 0 <= position1 <= (len(cached_row) - 1):
        element1 = cached_row[position1]
    if 0 <= position2 <= (len(cached_row) - 1):
        element2 = cached_row[position2]
    return element1 + element2


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists, where each list represents a row of Pascal's triangle.
    """
    if n <= 0:
        return []
    whole_thing = []
    cached_row = [1]
    row_count = 1
    whole_thing.append(cached_row)
    while row_count < n:
        row = [None] * (len(cached_row) + 1)  # allocate strictly the memory needed
        limit = len(cached_row)
        for col in range(0, limit + 1, 4):
            element = try_get_elements_c1_c2(col, cached_row)
            row[col] = element

            if col + 1 <= limit:
                element = try_get_elements_c1_c2(col + 1, cached_row)
                row[col + 1] = element

            if col + 2 <= limit:
                element = try_get_elements_c1_c2(col + 2, cached_row)
                row[col + 2] = element

            if col + 3 <= limit:
                element = try_get_elements_c1_c2(col + 3, cached_row)
                row[col + 3] = element
        cached_row = row
        row = []
        row_count += 1
        whole_thing.append(cached_row)
    return whole_thing
