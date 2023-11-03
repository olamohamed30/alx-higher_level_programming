#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    all_names = dir(hidden_4)
    filtered_names = [name for name in all_names if not name.startswith('__')]
    for name in sorted(filtered_names):
        print(name)
