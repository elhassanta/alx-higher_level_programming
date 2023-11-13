#!/usr/bin/python3
import os
with open("text.txt", mode="w", encoding="utf-8") as file1:
    file1.write("Some random text\nbecause write doesn't add new line\nlast line of file")
#let's open the file for reading this time

with open("text.txt", encoding="utf-8") as file1:
    for line in file1:
        print(line, end="")
    """ 
    print("file.read():", file1.read())#read all the file and put it into a string
    print("-*" * 50)
    print("file.readline(): ",file1.readline())#this read only one line
    print("-*" * 50)
    print("file.readlines() ",file1.readlines())#this read all lines in file and put them into a list
    #each one of those methods start from the end of its previous"""

