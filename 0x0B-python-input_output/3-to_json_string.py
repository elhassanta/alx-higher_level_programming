#!/usr/bin/python3
"""this is my code"""


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    data = pickle.dumps(my_obj)
    return base64.b64encode(data).decode()
