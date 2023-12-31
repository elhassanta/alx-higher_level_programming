#!/usr/bin/python3
"""defining a class"""


class Square:
    """this is the begining of the square class"""
    def __init__(self, size=0, position=(0, 0)):
        """this the constroctor"""
        self.size = size
        self.position = position

    def get_size(self):
        return (self.size)

    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            if i < self.size - 1:
                print("")
        print("")

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
