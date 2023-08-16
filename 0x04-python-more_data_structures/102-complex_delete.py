#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    list_of_key = []
    for k, v in a_dictionary.items():
        if v == value:
            list_of_key.append(k)
    for k in list_of_key:
        del a_dictionary[k]
    return a_dictionary
