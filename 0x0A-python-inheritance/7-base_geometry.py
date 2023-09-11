#!/usr/bin/python3
"""model's place"""


class BaseGeometry:
    """this is an empty class"""
    def area(self):
        """this method will calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this function will validate value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name)) 
