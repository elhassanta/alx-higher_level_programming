#!/usr/bin/python3
class MyList(list):
    """this class will inherit lis class"""

    def print_sorted(self):
        print(sorted(self))
