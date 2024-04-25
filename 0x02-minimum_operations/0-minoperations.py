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

    arr = [float('inf')] * (n + 1)
    arr[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0 and arr[j] + i // j < arr[i]:
                arr[i] = arr[j] + i // j

    return arr[n] if arr[n] != float('inf') else 0
