#!/usr/bin/python3
def element_at(my_list, idx):
    """My function that retrieve an elemt

    Args:

    my_list: parameter list of ineger
    idx: index of element to retrieve

    Return:

    return the element at index

    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
