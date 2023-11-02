#!/usr/bin/python3
import sys

if __name__ == "__main__":
    narg = len(sys.argv) - 1
    if narg == 0:
        print("0 arguments.")
    elif narg == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(narg))
        for i in range(1, narg + 1):
            print("{}: {}".format(i, sys.argv[i]))
