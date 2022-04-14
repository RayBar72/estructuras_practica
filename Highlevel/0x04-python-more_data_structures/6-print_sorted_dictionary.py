#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary):
        print(k, end=": ")
        print(a_dictionary[k])
