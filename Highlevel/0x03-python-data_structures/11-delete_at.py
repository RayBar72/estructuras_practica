#!/usr/bin/python3

from argparse import _MutuallyExclusiveGroup
from re import M


def delete_at(my_list=[], idx=0):
    l = len(my_list)
    if idx >= l or idx < 0:
        return my_list
    else:
        del my_list[idx]
    return my_list