#!/usr/bin/python3
def print_last_digit(number):
lds = str(number)[-1]
ld = int(lds) if number >= 0 else -int(lds)
print(ld)
