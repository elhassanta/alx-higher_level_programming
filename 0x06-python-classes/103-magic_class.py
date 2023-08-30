#!/usr/bin/python3
import math

class MagicClass:

    def __init__(self, radius=0):

        if type(radius) is not float or type(radius) is not int:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        return ((math.pi) * self._MagicClass_radius ** 2)

    def circumference(self):
        return (2 * (math.pi) * self._MagicClass_radius)
