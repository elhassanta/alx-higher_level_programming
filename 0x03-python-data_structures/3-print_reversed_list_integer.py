#!/usr/bin/python3
# 3-print_reversed_list_integer.py
def print_reversed_list_integer(my_list=[]):
    """My function print list at reverse ordre"""
    rev_list = my_list[:]
    rev_list = rev_list.reverse()
    for index in range(len(rev_list)):
        print("{:d}".format(rev_list[index]))
