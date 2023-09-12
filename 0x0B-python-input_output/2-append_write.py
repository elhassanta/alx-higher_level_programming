#!/usr/bin/python3
"""this is first comment"""


def append_write(filename="", text=""):
    """this my appending function into a text file"""
    if type(filename).__name__ == str.__name__:
        with open(filename, mode="a", encoding="utf-8") as file1:
            return file1.write(text)
