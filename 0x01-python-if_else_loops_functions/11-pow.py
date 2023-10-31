#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (a ** abs(b))
    else:
        res = 1
        for _ in range(b):
            res *= a
            return res
