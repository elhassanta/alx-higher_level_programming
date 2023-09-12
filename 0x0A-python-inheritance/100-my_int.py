#!/usr/bin/python3
"""this is right place of my comment for model"""


class MyInt(int):
    """this my in custome class"""

    def __init__(self, value):
        """this is my constructor"""
        if type(value).__name__ != int.__name__:
            raise TypeError("value must be integer")
        self.value = value
