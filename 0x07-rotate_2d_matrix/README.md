# Rotate 2D Matrix

This project provides a function to rotate a 2D matrix by 90 degrees clockwise.

```python
def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise.

    Args:
    matrix (list of list of int): The 2D matrix to rotate. It must be a square matrix (n x n).

    Returns:
    None: The matrix is modified in place.
    """
```

## Algorithm
1. Transpose the matrix: Convert all rows to columns and vice versa by swapping elements.
2. Reverse each row: Convert the transposed matrix into the final rotated matrix by reversing each row.

## Example
### Input
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### Output
```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## Usage
1. Ensure you have Python installed on your system.
2. Save the function code in a Python file, e.g., rotate_2d_matrix.py.
3. Call the function with an n×n matrix as input.

# Example Code:
```python
#!/usr/bin/env python3

def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise"""
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    rotate_2d_matrix(matrix)

    print("\nRotated Matrix:")
    for row in matrix:
        print(row)
```

# Output
```python
Original Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Rotated Matrix:
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
```

# Complexity
- Time Complexity: O(n2)
- Space Complexity:  O(1)

The algorithm operates in quadratic time relative to the number of elements in the matrix and uses a constant amount of extra space.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the script using Python.

## Usage

Here is a quick example of how to use the function:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_matrix(matrix)