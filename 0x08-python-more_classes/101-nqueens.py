#!/usr/bin/python3
"""this is our model that contains info"""

import sys


def main():
    """Check the number of command-line arguments"""
    exit = sys.exit
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    argv = sys.argv
    try:
        N = int(argv[1])
    except Exception as err:
        N = str()
        print(err)
    if not isinstance(N, int):
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)


if __name__ == "__main__":
    main()
