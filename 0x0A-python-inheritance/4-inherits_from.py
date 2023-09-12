#!/usr/bin/python3
"""this is the place of my models"""


def inherits_from(obj, a_class):
    """this function check if a model is a child or instance of that class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
