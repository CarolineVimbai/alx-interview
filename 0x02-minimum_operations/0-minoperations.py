#!/usr/bin/python3
"""
calculates the fewest number of operations 
"""


def minOperations(n):
    """
    Returns an integer
    """
    operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations
