#!/usr/bin/python3
"""this is my code"""
import json


def save_to_json_file(my_obj, filename):
    """function that returns the JSON representation of an object (string)"""
    obj_string = json.dumps(my_obj)
    with open(filename, mode = "w", encoding="utf-8") as file1:
        file1.write(obj_string)
        file1.close()
