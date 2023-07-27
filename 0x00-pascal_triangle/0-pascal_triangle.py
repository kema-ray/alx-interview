#!/usr/bin/python3
"""
Module for Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row containing just 1

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element of each row is always 1

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])  # Calculate middle elements of the row

        new_row.append(1)  # Last element of each row is always 1
        triangle.append(new_row)

    return triangle
