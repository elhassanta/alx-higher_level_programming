#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        tot_error = "Exception: " + str(err) + "\n"
        sys.stderr.write(tot_error)
        return False
    except TypeError as err:
        tot_error = "Exception: " + str(err) + "\n"
        sys.stderr.write(tot_error)
        return False
