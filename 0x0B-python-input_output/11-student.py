#!/usr/bin/python3
"""this is my class models"""


class Student:
    """this is my class struct"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """unction that returns the dictionary description with simple
        data structure (list, dictionary,string, integer and boolean)
        for JSON serialization of an object"""
        dict_attributes = self.__dict__
        dic = {}
        dic1 = {}
        for k, v in dict_attributes.items():
            if isinstance(v, (int, list, dict, bool, str)):
                if attrs is not None:
                    if k in attrs:
                        dic[k] = v
                else:
                    dic[k] = v
        return dic

    def reload_from_json(self, json):
        dic = self.to_json()
        for k, v in json.items():
            if k in dic.keys():
                dic[k] = v
