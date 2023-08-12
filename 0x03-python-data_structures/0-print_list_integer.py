#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """My print integer function

    Args:
        my_list: list of integer
    """
    if my_list != []:
        for number in my_list:
            print("{}".format(number))
