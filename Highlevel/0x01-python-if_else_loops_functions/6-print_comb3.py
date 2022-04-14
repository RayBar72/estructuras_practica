#!/usr/bin/python3
lista = []
for x in range(0, 10):
    for y in range(0, 10):
        z = str(x) + str(y)
        if y > x and z != "89":
            print("{}".format(z), end=", ")
print("89")