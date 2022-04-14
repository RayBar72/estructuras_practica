#!/usr/bin/python3

def max_integer(my_list=[]):
    l = len(my_list)
    x = 0
    if l == 0:
        return None
    else:
        lists = sorted(my_list)
        x = lists[-1]
        x = str(x)
        x = int(x)
        return x