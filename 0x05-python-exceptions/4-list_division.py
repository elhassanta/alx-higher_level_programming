#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    element_added = 0
    elements = list()
    print(list_length)
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            elements.append(result)
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            continue
    return elements


my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
print(max(len([1, 2, 3]), len([2, 3, 4])))
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
