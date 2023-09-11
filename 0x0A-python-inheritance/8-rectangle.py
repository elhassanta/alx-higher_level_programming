#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""this is the place of my models"""


class Rectangle(BaseGeometry):
    """this my rectangle class"""
    def __init__(self, width, height):
        """this is m y constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
