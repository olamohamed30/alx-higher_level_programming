#!/usr/bin/python3
import hidden_4

if __name__ == "_main_":
    alln = dir(hidden_4)
    filt = [name for name in alln if not name.startswith('__')]
    for name in sorted(filt):
        print(name)
