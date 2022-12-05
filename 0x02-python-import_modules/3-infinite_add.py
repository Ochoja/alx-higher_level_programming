#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arg = len(sys.argv) - 1

    if (arg < 1):
        print(0)
    else:
        total = 0
        i = 1
        while i <= arg:
            total += int(sys.argv[i])
            i += 1
        print(total)
