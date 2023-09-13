#!/usr/bin/python3
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
"""


def print_status(size, status):
    """Print status"""
    print("File size: {}".format(size))
    arr_keys = sorted(status)
    for key in arr_keys:
        print("{}: {}".format(key, status[key]))


if __name__ == "__main__":
    import sys

    count = 1
    size = 0
    status_codes = dict()
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            if count == 10:
                print_status(size, status_codes)
                count = 1
            else:
                count += 1

            words = line.split()

            try:
                size += int(words[-1])
            except (IndexError, ValueError):
                pass

            try:
                if words[-2] in valid_codes:
                    if status_codes.get(words[-2], -1) == -1:
                        status_codes[words[-2]] = 1
                    else:
                        status_codes[words[-2]] += 1
            except IndexError:
                pass

        print_status(size, status_codes)

    except KeyboardInterrupt:
        print_status(size, status_codes)
    raise
