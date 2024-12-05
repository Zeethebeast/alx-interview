#!/usr/bin/python3
from typing import List

"""
Create a function def
island_perimeter(grid):
that returns the perimeter of the
island described in grid
"""
def island_perimeter(grid: List[List[int]]) -> int:
    """
    Calculate the perimeter of the island in a grid.

    Args:
        grid (List[List[int]]): A 2D grid of integers representing land and water.

    Returns:
        int: The perimeter of the island.
    """
    # Dimensions of the grid
    length_row = len(grid)
    length_col = len(grid[0])

    # Initialize perimeter and shared edge count
    perimeter = 0
    connection = 0

    for x in range(length_row):
        for y in range(length_col):
            # Check if the current cell is land
            if grid[x][y] == 1:
                perimeter += 4  # Add 4 sides for a land cell

                # Check for connections (shared edges) with adjacent cells
                if x > 0 and grid[x - 1][y] == 1:  # Land above
                    connection += 1
                if y > 0 and grid[x][y - 1] == 1:  # Land to the left
                    connection += 1

    # Subtract twice the number of connections from the total perimeter
    return perimeter - (connection * 2)
