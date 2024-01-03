#!/usr/bin/python3
"""
Python script taht sends a request to a url and displays the value of
X-Request-Id variable found in the header of the response.
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    req = urllib.request
    with req.urlopen(argv[1]) as resp:
        print('{}'.format(resp.info().get('X-Request-Id')))
