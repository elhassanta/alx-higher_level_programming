#!/usr/bin/python3
"""defining a class"""


class Square:
    """this is the begining of the square class"""
    def __init__(self, value=0):
        """this the constroctor"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def get_size(self):
        return (self.size)

    def area(self):
        """this methode will calculate the area of a square"""
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        if self.size < 0:
            raise ValueError("size must be >= 0")
        area = (self.size * self.size)
        return area

    def get_size(self):
        return (self.size)

    def set_size(self, value=0):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value
