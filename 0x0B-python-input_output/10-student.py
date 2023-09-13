#!/usr/bin/python3
"""this is my class models"""


class Student:
    """this is my class struct"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """unction that returns the dictionary description with simple
        data structure (list, dictionary,string, integer and boolean)
        for JSON serialization of an object"""
        dict_attributes = self.__dict__
        dic = {}
        for k, v in dict_attributes.items():
            if isinstance(v, (int, list, dict, bool, str)):
                dic[k] = v
        return dic
