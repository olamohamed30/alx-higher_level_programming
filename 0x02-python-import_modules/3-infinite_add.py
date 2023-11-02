#!/usr/bin/python3
import sys

if __name__ == "__main__":
    summ = 0
    args = len(sys.argv)-1
    if args == 0:
        print("0")
    else:
        for i in range(args):
            summ += int(sys.argv[i+1])
        print("{}".format(summ))

