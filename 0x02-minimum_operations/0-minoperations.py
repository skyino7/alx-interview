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

    num_op = 0
    min_op = 2

    while n > 1:
        if n % min_op == 0:
            num_op += min_op
            n /= min_op
        else:
            min_op += 1

    return num_op
