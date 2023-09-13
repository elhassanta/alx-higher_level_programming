#!/usr/bin/python3
"""this is my class models"""


def pascal_triangle(n):
    """Technical interview preparation"""
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        line = [1]
        for i in range(len(tri) - 1):
            line.append(tri[i] + tri[i + 1])
        line.append(1)
        triangle.append(line)
    return triangle
