#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""imported my model to use"""


class Square(Rectangle):
    """this is my square class it will enhirite some methods"""
    def __init__(self, size):
        """this is the constcture for a sauqre"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """this method count area of a square"""
        return (self.__size ** 2)
