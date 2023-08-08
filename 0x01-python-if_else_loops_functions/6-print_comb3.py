#!/usr/bin/python3
for number in range(0, 10):
    for i in range(number + 1, 10):
        if i == 9 and number == 8:
            print("{}{}".format(number, i))
        else:
            print("{}{},".format(number, i), end=" ")
