#!/usr/bin/python3
"""this is the right place to describe my model"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this is my square class it will enhirite some methods"""

    def __init__(self, size):
        """this is the constcture for a sauqre"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """this method count area of a square"""
        return (self.__size ** 2)

    def __str__(self):
        """this is a function cosume the string descreptor"""
        return "[Square] {}/{}".format(self.size, self.size)
