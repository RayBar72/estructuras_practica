#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
if number < 0:
    last = "-" + num[-1:]
else:
    last = num[-1:]
ld = int(last)
print("Last digit of {} is {}".format(number, last), end=" ")
if ld == 0:
    print("and is 0")
elif ld > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
