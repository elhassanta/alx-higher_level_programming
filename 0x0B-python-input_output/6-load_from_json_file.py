#!/usr/bin/python3
"""this place ofcomment that describes my models"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding="utf-8") as file1:
        str1 = file1.read()
        return json.loads(str1)
