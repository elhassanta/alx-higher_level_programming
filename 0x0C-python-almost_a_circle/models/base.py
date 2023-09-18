#!/usr/bin/python3
"""this my models' place"""
import json

class Base:
    """my grand parent class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """my Base constructor class' method"""
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """this is my method to transform list to json string"""
        if list_dictionaries == None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this is my class method to write int files"""
        file_name = cls.__name__ + ".json"
        list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, mode="w", encoding="utf-8") as file1:
            string = json.dumps(list_objs)
            file1.write(string)

    def from_json_string(json_string):
        """this method will convert json string to an object"""
        if json_string == None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """that returns an instance with all attributes already"""
        id = dictionary["id"]
        x = dictionary["x"]
        y = dictionary["y"]
        if cls.__name__ == "Rectangle":
            width = dictionary["width"]
            height = dictionary["height"]
            return cls(width, height, x, y, id)
        if cls.__name__ == "Square":
            size = dictionary["size"]
            return cls(size, x, y, id)

    @classmethod
    def load_from_file(cls):
        """this function that returns a list of instances"""
        file_name = cls.__name__ + ".json"
        my_list = []
        with open(file_name, mode="r", encoding="utf-8") as file:
            string = file.read()
            list_of_objs = json.loads(string)
            if cls.__name__ == "Rectangle":
                for dct in list_of_objs:
                    width = dct["width"]
                    height = dct["height"]
                    x = dct["x"]
                    y = dct["y"]
                    id = dct["id"]
                    my_list.append(cls(width, height, x, y, id))
            else:
                for dct in list_of_objs:
                    size = dct["size"]
                    x = dct["x"]
                    y = dct["y"]
                    id = dct["id"]
                    my_list.append(cls(size, x, y, id))
        return my_list 
