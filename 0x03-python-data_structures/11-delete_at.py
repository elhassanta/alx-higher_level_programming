#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """My function deletes the item at a specific position in a list.

    Args:

    my_list: list of integers
    idx: index of element to remove

    Return:

    return a new list of integers
    """
    if idx <= 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
