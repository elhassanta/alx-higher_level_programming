#!/usr/bin/python3
import sys
write = sys.stderr.write


def safe_function(fct, *args):
    (arg1, arg2) = args
    try:
        result = fct(arg1, arg2)
        return result
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
