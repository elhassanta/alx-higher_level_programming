#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print(0)
    else:
        length = 1
        add = 0
        while (length < len(argv)):
            add += int(argv[length])
            length += 1
        print("{}".format(add))
