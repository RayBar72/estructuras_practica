#!/usr/bin/python3

def print_last_digit(number):
	number = str(number)
	n = int(number[-1:])
	print("{}".format(n), end="")
	return n