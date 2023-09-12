#!/usr/bin/python3
"""this is a comment for my model"""


def read_file(filename=""):
    """this my function which open a file"""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        str1 = myFile.read()
