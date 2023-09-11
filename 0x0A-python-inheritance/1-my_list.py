#!/usr/bin/python3
"""this is the place of our models"""


class MyList(list):
    """this class will inherit lis class"""

    def print_sorted(self):
        """this methode print a sorted array"""
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/1-my_list.txt")
