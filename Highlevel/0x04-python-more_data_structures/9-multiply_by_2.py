#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = {}
    for k in a_dictionary:
        temp = {k: a_dictionary[k] * 2}
        new.update(temp)
    return new