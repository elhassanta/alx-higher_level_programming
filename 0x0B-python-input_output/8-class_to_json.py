#!/usr/bin/python3
"""this is a comment for my models"""
to_json_string = __import__('3-to_json_string').to_json_string

def class_to_json(obj):
    """unction that returns the dictionary description with simple
    data structure (list, dictionary,string, integer and boolean)
    for JSON serialization of an object"""
    
    dict_attributes = vars(a)
    return to_json_string(dict_attributes)
