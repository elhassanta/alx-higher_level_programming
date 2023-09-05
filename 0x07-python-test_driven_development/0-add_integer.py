#!/usr/bin/python3
"""this is my model"""


def add_integer(a, b=98):
    """this is my function"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
