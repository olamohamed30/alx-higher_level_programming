#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    s1 = s2 = 0
    if len(tuple_a) > 0:
        s1 += tuple_a[0]
    if len(tuple_b) > 0:
        s1 += tuple_b[0]
    if len(tuple_a) > 1:
        s2 += tuple_a[1]
    if len(tuple_b) > 1:
        s2 += tuple_b[1]
    return (s1, s2)

