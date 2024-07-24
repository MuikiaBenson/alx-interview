#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """generates pascal's triangle up to the nth row
       function returns a list of lists, where inner
       row represents a row in Pascal's Triangle.
       Each number is the sum of two numbers directly
       above it in the previous row.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
