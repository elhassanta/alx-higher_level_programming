#!/usr/bin/python3
"""
That class inherits from the int class
"""


class MyInt(int):
    """
    class MyInt inherit from the int class
    """
    def __eq__(self, value):
        """overide int __eq__"""
        return self.real == value

    def __ne__(self, value):
        """overide __ne__ method"""
        return self.real != value


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
