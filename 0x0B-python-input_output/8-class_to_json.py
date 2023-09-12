#!/usr/bin/python3
"""this is a comment for my models"""
import json


def class_to_json(obj):
    """unction that returns the dictionary description with simple
    data structure (list, dictionary,string, integer and boolean)
    for JSON serialization of an object"""
    dict_attributes = vars(obj)
    return json.dumps(dict_attributes)
