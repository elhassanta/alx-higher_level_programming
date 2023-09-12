#!/usr/bin/python3
"""
That class inherits from the int class
"""


class MyInt(int):
    """
    class MyInt inherit from the int class
    """
    def __int__(self, value=0):
        self.value = value


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
