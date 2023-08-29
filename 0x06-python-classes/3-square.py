#!/usr/bin/python3
"""defining a class"""


class Square:
    """this is the begining of the square class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """this methode will calculate the area of a square"""
        return (self.__size ** 2)
