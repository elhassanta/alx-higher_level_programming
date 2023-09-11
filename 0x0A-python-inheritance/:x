#!/usr/bin/python3
"""this is place of my models"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this my rectangle class"""
    def __init__(self, width, height):
        """this is m y constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """this function count area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """this function give you customise string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
