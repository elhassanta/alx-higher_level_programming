#!/usr/bin/python3
import sys
write = sys.stderr.write


def safe_function(fct, *args):
    (arg1, arg2) = args
    try:
        result = fct(arg1, arg2)
        return result
    except IndexError as err:
        tot_error = "Exception: " + str(err) + "\n"
        write(tot_error)
        return None
    except TypeError as err:
        tot_error = "Exception: " + str(err) + "\n"
        write(tot_error)
        return None
    except ZeroDivisionError as err:
        tot_error = "Exception: " + str(err) + "\n"
        write(tot_error)
        return None
