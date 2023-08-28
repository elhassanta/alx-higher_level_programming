#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    element_added = 0
    elements = list()
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            elements.append(result)
        except IndexError:
            print("out of range")
            elements.append(0)
        except ZeroDivisionError:
            print("division by 0")
            elements.append(0)
        except TypeError:
            print("wrong type")
            elements.append(0)
        finally:
            continue
    return elements
