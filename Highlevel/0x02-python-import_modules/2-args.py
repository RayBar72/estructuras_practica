#!/usr/bin/python3
from sys import argv


l = len(argv)
if l == 1:
    print("0 arguments.")
elif l == 2:
    print("1 argument:")
    print("1: {}".format(argv[1]))
else:
    print("{} arguments:".format(l - 1))
    for x in range(1, l):
        print("{}: {}".format(x, argv[x]))
