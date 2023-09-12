#!/usr/bin/python3
"""this is my code"""
import json


def save_to_json_file(my_obj, filename):
    """function that returns the JSON representation of an object (string)"""
    obj_string = json.dumps(my_obj)
    with open(filename, mode = "w", encoding="utf-8") as file1:
        file1.write(obj_string)
        file1.close()
filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

