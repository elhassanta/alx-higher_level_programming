#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """My function replace an element in a list at index idx

    Args:

    my_list: parameter list to modify
    idx: pramter integer at index
    element: element to be replace with

    Return: return a list
    """
    if idx < 0 or idx > len(my_list):
        return my_list
    my_list[idx] = int(element)
    return my_list
