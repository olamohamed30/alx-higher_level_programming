#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lds = str(number)[-1]

ld = int(lds) if number >= 0 else -int(lds)

print("Last digit of {} is {}".format(number, ld), end=" ")

if ld > 5:
    print("and is greater than 5")
elif ld == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
