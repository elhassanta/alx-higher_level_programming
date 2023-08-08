#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    l = 0
    for letter in str:
        if l != n:
            str1 += letter
        l += 1
    return str1

