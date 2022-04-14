#!/usr/bin/python3

from re import M


def square_matrix_simple(matrix=[]):
    m = [[x ** 2 for x in row] for row in matrix]
    return m
