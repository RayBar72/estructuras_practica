#!/usr/bin/python3

def uppercase(str):
	a = ""
	for s in str:
		s = ord(s)
		if s >= 97 and s <= 122:
			s -= 32
		s = chr(s)
		print("{}".format(s), end="")
	print("")
