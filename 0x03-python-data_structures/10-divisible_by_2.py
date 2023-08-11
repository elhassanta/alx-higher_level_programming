#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """My function finds all multiples of 2 in a list.

    Arg:

    my_list: list of integer

    Return:

    return list of intigers
    """
    if len(my_list) == 0:
        return []
    new_list = list()
    for element in my_list:
        if element % 2 == 0:
            new_list.append(True)
            continue
        new_list.append(False)
    return new_list
