#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
    str1 = f'Last digit of {number} is {last_digit} and '
else:
    last_digit = (-number) % 10
    last_digit = 0 - last_digit
    str1 = f'Last digit of {number} is {last_digit} and '
if last_digit == 0:
    str1 += "is 0"
elif last_digit > 5:
    str1 += "is greater than 5"
elif last_digit < 6:
    str1 += "is less than 6 and not 0"
print(str1)
