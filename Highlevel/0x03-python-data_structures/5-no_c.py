#!/usr/bin/python3

def no_c(my_string):
    s = ""
    for m in my_string:
        n = ord(m)
        if n != 67 and n != 99:
            s += m
    return s