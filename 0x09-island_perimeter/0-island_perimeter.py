#!/usr/bin/python3
"""this module contains a function that solves the island perimiter problem"""


def island_perimeter(grid):
    """
    this function takes a grid n * n  that represent
    an island and determins its perimiter
    """
    if len(grid) > 100:
        return 0
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == len(grid[0])-1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter
