#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """This function replaces an element in a list at a
    specific position without modifying the original list

    Args:

    my_list: parameter list of integer
    idx: parameter integer index of an element
    element: parameter element to change with

    Return:

    return a new list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    return my_list[:idx] + [element] + my_list[idx + 1:]
