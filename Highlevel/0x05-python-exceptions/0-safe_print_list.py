#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for m in range(x):
            print("{}".format(my_list[m]), end="")
            i += 1
    except(IndexError, ValueError, TypeError):
        pass
    finally:
        print("")
        return i