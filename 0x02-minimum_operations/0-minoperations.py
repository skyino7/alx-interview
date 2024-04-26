#!/usr/bin/python3
"""
Given a number n, write a method that calculates
the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Function that calculates the fewest number of operations
    """

    if n == 1:
        return 0

    if n % 2 == 1:
        return minOperations(n - 1) + 1
    else:
        return minOperations(n / 2) + 2
