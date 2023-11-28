#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        new_row = []
        for i in range(len(triangle[-1]) + 1):
            left_num = triangle[-1][i - 1] if i > 0 else 0
            right_num = triangle[-1][i] if i < len(triangle[-1]) else 0
            new_row.append(left_num + right_num)

        triangle.append(new_row)

    return triangle
