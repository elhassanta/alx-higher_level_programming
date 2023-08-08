#!/usr/bin/python3
def uppercase(str1):
    str2 = ""
    for letter in str1:
        if ord(letter) > ord('a') and ord(letter) < ord('z'):
            str2 += chr(ord('A') + (ord(letter) - ord('a')))
        else:
            str2 += letter
