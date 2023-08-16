#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (0)
    arr_top = [(a[0] * a[1]) for a in my_list]
    arr_down = [a[1] for a in my_list]
    return (sum(arr_top) / sum(arr_down))
