#!/usr/bin/python3
"""this is my code"""
import pickle


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    if type(my_obj).__name__ == set.__name__:
        raise TypeError("{} is not JSON serializable".format(my_obj))
    serialized_data = pickle.dumps(my_obj)
    return pickle.loads(serialized_data)
