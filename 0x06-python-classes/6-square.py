#!/usr/bin/python3
"""
This class is used to Create object of type Square
"""


class Square:
    """
    This class is used to define a square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        This mothod initialize an object of the class square
        """
        errstr = "position must be a tuple of 2 positive integers"
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size mst be >= 0")
        else:
            raise TypeError("size must be an integer")

        if isinstance(position, tuple) and len(position) == 2:
            if isinstance(position[0], int) and isinstance(position[1], int):
                pass
            else:
                raise TypeError(errstr)
            if position[0] < 0 or position[1] < 0:
                raise ValueError("position must be a tuple of \
2 positive integers")
            self.__position = tuple(position)
        else:
            raise TypeError(errstr)

    def area(self):
        """
        calculate the area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        get the value of the private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size is function sets a value in the attribute size
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be integer")

    def my_print(self):
        """
        print a square in the stdout with #
        """
        if self.position[1] != 0 and self.__size != 0:
            print("\n" * self.position[1], end='')
        for i in range(self.__size):
            if self.__position[0] != 0:
                print(" " * self.__position[0], "#" * self.__size, sep='')
            else:
                print("#" * self.__size)
        if (self.__size == 0):
            print()

    @property
    def position(self):
        """
        return the value of the attribute position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Write a class Square that defines a square by
        """
        errstr = "position must be a tuple of 2 positive integers"
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                self.__position = tuple(value)
            else:
                raise TypeError(errstr)
        else:
            raise TypeError(errstr)
