#!/usr/bin/python3
"""this is my code"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    serialized_data = json.dumps(my_obj)
    return json.loads(serialized_data)
