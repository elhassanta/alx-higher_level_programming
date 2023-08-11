#!/usr/bin/python3
def no_c(my_string):
    """My function remove c and C from my string

    Arg:

    my_string: parameter string that you want to modify
    """
    str1 = ""
    for string in my_string:
        if string not in "Cc":
            str1 += string
