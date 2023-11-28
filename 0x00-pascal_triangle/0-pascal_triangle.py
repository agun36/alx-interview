#!/usr/bin/python3

def pascal_triangle(n):
    """
    Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(n - 1):
        row = [1]
        for j in range(len(triangle[-1]) - 1):
            row.append(triangle[-1][j] + triangle[-1][j + 1])
        row.append(1)
        triangle.append(row)
    return triangle