#!/usr/bin/python3
"""this is my model"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    (UTF8) and returns the number of characters written"""
    if filename != "" or not isinstance(filename, str):
        with open(filename, mode="w", encoding="utf-8") as file1:
            file1.write(text)
            file1.close()
