#!/usr/bin/python3
"""
Returns the perimeter of the
island described in grid
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): A 2D list representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    """Get the dimensions of the grid"""
    rows = len(grid)
    cols = len(grid[0])

    """Loop through each cell in the grid"""
    for row in range(rows):
        for col in range(cols):
            """check all four sides"""
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
