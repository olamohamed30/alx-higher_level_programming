#!/usr/bin/python3
import sys
summ = 0
for i in sys.argv[1:]:
    num = int(i)
    summ += num
print(summ)
