#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """My function print list in revers order

    Args:

    my_list: list of antegers

    """
    for index in range(len(my_list) - 1, -1, -1):
        print("{}".format(my_list[index]))
