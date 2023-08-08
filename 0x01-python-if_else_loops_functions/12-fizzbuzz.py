#!/usr/bin/python3
def fizzbuzz():
    str1 = ""
    for number in range(1, 101):
        if (number % 3) == 0 and (number % 5) == 0:
            str1 += "FizzBuzz "
        elif (number % 3) == 0:
            str1 += "Fizz "
        elif (number % 5) == 0:
            str1 += "Buzz "
        else:
            str1 += "{} ".format(number)
    print(str1)
fizzbuzz()
