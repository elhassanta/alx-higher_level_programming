#!/usr/bin/python3
"""this the place for my models"""


def is_same_class(obj, a_class):
    """this function will return true if obj is instance of a given class"""
    if type(obj).__name__ == a_class.__name__:
        return True
    return False
