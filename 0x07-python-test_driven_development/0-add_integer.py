#!/usr/bin/python3
"""
Module to add to integers
"""


def add_integer(a, b=98):
    """
    add_integer: adds two integer and returns the result
    3
    """
    if a is None:
        return
    if type(a) in [int, float]:
        a = int(a)
        if type(b) in [int, float]:
            b = int(b)
            return a + b
        else:
            raise TypeError("b must be an integer")
    raise TypeError("a must be an integer")


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
