#!/usr/bin/python3
# 2-replace_in_list.py
def replace_in_list(my_list, idx, element):
    """My function replace an element in a list at index idx"""
    if idx >= 0 or idx < len(my_list):
        my_list[idx] = element
    return my_list
