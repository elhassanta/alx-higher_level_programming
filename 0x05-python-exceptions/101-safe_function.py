#!/usr/bin/python3
import sys
write = sys.stderr.write


def safe_function(fct, *args):
    (arg1, arg2) = args
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
    except ZeroDivisionError as err:
        tot_error = "Exception: " + str(err) + "\n"
        write(tot_error)
