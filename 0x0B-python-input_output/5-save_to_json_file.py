#!/usr/bin/python3
"""this is my code"""
import json


def save_to_json_file(my_obj, filename):
    """function that returns the JSON representation of an object (string)"""
    with open(filename, mode="w", encoding="utf-8") as file1:
        obj_string = json.dumps(my_obj)
        return file1.write(obj_string)
