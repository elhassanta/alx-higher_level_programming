#!/usr/bin/python3
"""this is comment for my models"""
import sys


read = sys.stdin.readline
i = 1
a = []
while i < 3:
    b = read()
    a.append(b)
    i = i + 1
total_size = 0
for j in a:
    elem = j.split()[8]
    print(elem)
    total_size += int(elem)
print(total_size)
