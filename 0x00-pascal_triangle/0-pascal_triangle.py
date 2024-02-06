#!/usr/bin/python3
"""Module returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n): 
    """lists a list of integers """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element is always 1
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
