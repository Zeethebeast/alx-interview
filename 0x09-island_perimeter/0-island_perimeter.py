#!/usr/bin/python3
from typing import List

"""
Create a function def
island_perimeter(grid):
that returns the perimeter of the
island described in grid
"""

def island_perimeter(grid: List[List[int]]) -> int:
    length_row = len(grid)
    length_col = len(grid[0])

    perimeter = 0
    connection = 0

    for x in range(0, length_row):
        for y in range(0, length_col):

            if grid[x][y] == 1:
                perimeter += 4

                if x != 0 and grid[x -1][y] == 1:
                    connection +=1 
                if y != 0 and grid[x][y - 1] == 1:
                    connection += 1
    return perimeter - (connection * 2)
