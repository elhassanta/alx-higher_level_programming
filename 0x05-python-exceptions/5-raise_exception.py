#!/usr/bin/python3
def raise_exception():
    class TypeError(Exception):
        pass
    raise TypeError("error")
