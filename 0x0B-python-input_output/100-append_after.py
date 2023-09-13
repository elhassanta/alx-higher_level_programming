#!/usr/bin/python3
"""this is my models"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string"""
    new_file = ""
    with open(filename) as file1:
        for line in file1:
            new_file = new_file + line
            if search_string in line:
                new_file = new_file + new_string
    with open(filename, "w") as file1:
        file1.write(new_file)
