#!/usr/bin/python3

def search_replace(my_list, search, replace):
    i = 0
    new = []
    for m in my_list:
        if m == search:
            new.append(replace)
        else:
            new.append(m)
        i += 1
    return new