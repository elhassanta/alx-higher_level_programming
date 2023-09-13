#!/usr/bin/python3
"""this place ofcomment that describes my models"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    a = load_from_json_file("add_item.json")
except Exception as err:
    a = []
arguments = a + sys.argv[1:]
save_to_json_file(arguments, "add_item.json")
load_from_json_file("add_item.json")
