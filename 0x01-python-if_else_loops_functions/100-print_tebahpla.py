#!/usr/bin/python3
str1 = ""
number = ord('z')
while (number >= ord('a')):
    if number % 2 == 0:
        str1 += "{}".format(chr(number))
    else:
        str1 += "{}".format(chr(number - ord('a') + ord('A')))
    number -= 1
print(str1)
