#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new = my_list[:]
    l = len(my_list)
    if idx < 0 or idx >= l:
        return new
    else:
        new[idx] = element
        return new
