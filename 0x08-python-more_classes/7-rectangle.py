#!/usr/bin/python3
"""this is the discription model"""


class Rectangle:
    """this is a tamplate to create rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self,  width=0, height=0):
        """this is the constroctor method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def perimeter(self):
        """this method calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def area(self):
        """this method calculate the area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """this is the string method"""
        str1 = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                str1 = str1 + str(self.print_symbol)
            if i < self.__height - 1:
                str1 = str1 + "\n"
        return str1

    def __repr__(self):
        """ this method allow us to create a copy of an instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """this is going pop out in deletion"""
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

    def __eq__(self, other):
        """Equality comparison."""
        if isinstance(other, Square):
            return self.__size == other.__size
        return False

    def __lt__(self, other):
        """Less than comparison."""
        if isinstance(other, Square):
            return self.__size < other.__size
        return False

    def __ge__(self, other):
        """Greater than or equal to comparison."""
        if isinstance(other, Square):
            return self.__size >= other.__size
        return False
