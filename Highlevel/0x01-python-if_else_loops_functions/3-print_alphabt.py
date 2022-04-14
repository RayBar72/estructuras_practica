#!/usr/bin/python3

for x in range(97, 123):
    x = chr(x)
    if x != "q" and x != "e":
        print("{}".format(x), end="")