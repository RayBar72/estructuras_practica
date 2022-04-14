#!/usr/bin/python3

for x in range(0, 99):
    y = x
    x = hex(x)
    print("{} = {}".format(y, x))