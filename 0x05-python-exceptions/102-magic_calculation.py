#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1,3):
        try:
            if a > i:
                raise Exception("Too far")

            result += a ** b / i
            result += a + b
            break
    excpt Exception:
