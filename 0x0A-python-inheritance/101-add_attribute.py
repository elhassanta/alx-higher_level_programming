#!/usr/bin/python3
"""place of my comment model"""


def add_attribute(obj, attribute, value):
    """this function add attribute if it is possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
