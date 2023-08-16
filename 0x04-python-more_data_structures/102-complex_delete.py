def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    for k, v in a_dictionary.items:
        if v == value:
            del a_dictionry[k]
    return a_dictionary
