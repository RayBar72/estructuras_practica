#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for x in row:
            if i:
                print(" ", end="")
            print("{}".format(x), end="")
            i += 1
        print("")