#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
    """My print integer function

    Args:
        my_list: list of integer
    """
    for number in range(len(my_list)):
        print("{:d}".format(my_list(number)))
