#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidd = dir(hidden_4)
    for hid in hidd:
        if hid[0] != '_':
            print(hid)
