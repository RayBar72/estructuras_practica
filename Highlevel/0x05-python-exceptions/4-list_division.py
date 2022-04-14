#!/usr/bin/python3

from traceback import print_tb


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        try:
            a = my_list_1[x] / my_list_2[x]
        except(TypeError):
            print("wrong type")
            a = 0
        except(ZeroDivisionError):
            print("division by 0")
            a = 0
        except(IndexError):
            print("out of range")
            a = 0
        finally:
            new_list.append(a)
    return new_list
        