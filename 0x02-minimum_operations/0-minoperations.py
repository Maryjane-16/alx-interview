#!/usr/bin/python3
"""
calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    returns an integer
    """
    operation_count = 0
    operation_number = 2
    if type(n) is not int and n <= 0:
        return operation_count
    while n > 1:
        if n % operation_number == 0:
            operation_count += operation_number
            n //= operation_number
        else:
            operation_number += 1
    return operation_count