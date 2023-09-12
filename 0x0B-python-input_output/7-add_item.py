#!/usr/bin/python3
"""this place ofcomment that describes my models"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


arguments = sys.argv[1:]
save_to_json_file(arguments, "add_item.json")
load_from_json_file("add_item.json")
