#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != type(str()):
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list1 = list()
    for str1 in roman_string:
        list1.append(str1)
    list1.reverse()
    number = values[list1[0]]
    check = list1[0]
    for index in range(1, len(list1)):
        if values[list1[index]] >= values[check]:
            check = list1[index]
            number = number + values[list1[index]]
        else:
            number = number - values[list1[index]]
    return number
