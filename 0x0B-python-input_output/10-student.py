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
                if attrs != None:
                    if k in attrs:
                        dic[k] = v
                else:
                    dic[k] = v
        return dic
student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)
j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])
print(j_student_1)
print(j_student_2)
print(j_student_3)
