#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """My function add two tuples

    Args:

    tuple_a: first parameter tuple of integers
    tuple_b: second parameter tuple of integers

    Return:

    """
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    elif len(tuple_a) >= 2 and len(tuple_b) == 1:
        return (tuple_a[0] + tuple_b[0], tuple_a[1])
    elif len(tuple_a) >= 2 and len(tuple_b) == 0:
        return (tuple_a[0], tuple_a[1])
    elif len(tuple_a) == 1 and len(tuple_b) >= 2:
        return (tuple_a[0] + tuple_b[0], tuple_b[1])
    elif len(tuple_a) == 0 and len(tuple_b) >= 2:
        return (tuple_b[0], tuple_b[1])
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        return (tuple_a[0] + tupe_b[0], 0)
    else:
        return (0, 0)
