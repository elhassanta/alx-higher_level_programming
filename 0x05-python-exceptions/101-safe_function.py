#!/usr/bin/python3
import sys


write = sys.stderr.write
def safe_function(fct, *args):
    (arg1,arg2) = args
    print("ok *", arg1, arg2)
    try:
        result = fct(arg1, arg2)
        return result
    except IndexError as err:
        tot_error = "Exception: " + str(err) + "\n"
        write(tot_error)
    except TypeError as err:
        tot_error = "Exception: " + str(err) + "\n"
        write(tot_error)
    except ZeroDivisionError  as err:
        tot_error = "Exception: " + str(err) + "\n"
        write(tot_error)
def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))


def print_list(my_list, len):
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))

