#!/usr/bin/python3
"""this is a comment for my models"""


def class_to_json(obj):
    """unction that returns the dictionary description with simple
    data structure (list, dictionary,string, integer and boolean)
    for JSON serialization of an object"""
    dict_attributes = obj.__dict__
    dic = {}
    for k, v in dict_attributes:
        if isinstance(v,(int, list, dict, bool, str)):
            dic[k] = v
    return dic
