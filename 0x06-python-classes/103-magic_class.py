#!/usr/bin/python3
"""magic class"""

import math


class MagicClass:
    """ begining of magic class"""

    def __init__(self, radius=0):
        """constructor of disk class

        args:
            radius: param int or float
        """

        if type(radius) is not float and type(radius) is not int:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """this method calculate the erea"""
        return ((math.pi) * self.__radius ** 2)

    def circumference(self):
        """this method calculate the perimeter of disk"""
        return (2 * (math.pi) * self.__radius)
