#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.
"""
import sys


def isSafe(board, row, col, n):
    """
    Checks if the position is safe
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    # Check if there is a queen in the same column
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
    return True


def solve(board, row, n):
    """
    Solves the N-Queens problem
    """
    if row == n:
        # Print the solution
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'Q':
                    solution.append([i, j])
        solutions.append(solution)
        return
    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 'Q'
            solve(board, row + 1, n)
            board[row][col] = '.'


solutions = []
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [['.' for i in range(n)] for j in range(n)]
solve(board, 0, n)
for solution in solutions:
    print(solution)
