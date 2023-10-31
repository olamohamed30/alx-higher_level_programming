#!/usr/bin/python3
def pow(a, b):
    res = 1
    if b == 0:
        return 1
    elif b < 0:
        a = 1 / a
        b = -b
    for i in range(b):
        res *= a
    return res
