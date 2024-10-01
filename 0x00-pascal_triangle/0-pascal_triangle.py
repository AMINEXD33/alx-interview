#!/usr/bin/python3


def try_get_elements_C1_C2(current_col: int, cached_row):
    position1 = current_col - 1
    position2 = current_col
    element1 = 0
    element2 = 0
    if position1 >= 0 and position1 <= (len(cached_row) - 1):
        element1 = cached_row[position1]
    if position2 >= 0 and position2 <= (len(cached_row) - 1):
        element2 = cached_row[position2]
    return element1 + element2


def pascal_triangle(n):
    if n <= 0:
        return []
    cached_row = [1]
    row_count = 0
    while row_count < n:
        row = [None] * (len(cached_row) + 1)  # allocate strictly the memory needed
        limit = len(cached_row)
        for col in range(0, limit + 1, 4):
            element = try_get_elements_C1_C2(col, cached_row)
            row[col] = element

            if col + 1 <= limit:
                element = try_get_elements_C1_C2(col + 1, cached_row)
                row[col + 1] = element

            if col + 2 <= limit:
                element = try_get_elements_C1_C2(col + 2, cached_row)
                row[col + 2] = element

            if col + 3 <= limit:
                element = try_get_elements_C1_C2(col + 3, cached_row)
                row[col + 3] = element
        cached_row = row
        row = []
        row_count += 1
        print(cached_row)


pascal_triangle(1400)
