#!/usr/bin/python3
# 3-print_reversed_list_integer.py
def print_reversed_list_integer(my_list=[]):
    """My function print list at reverse ordre"""
    for index in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[index]))
