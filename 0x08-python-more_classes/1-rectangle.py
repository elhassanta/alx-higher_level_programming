#!/usr/bin/python3
class Rectangle:
    """this is a tamplate to create rectangle object"""

    def __init__(self,  width=0, height=0):
        """this is the constroctor method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """this the getter method of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """this is the setter method of height"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """this the getter method of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """this is the setter method of height"""
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
