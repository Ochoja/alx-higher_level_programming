#!/usr/bin/python3

import sys

arg = len(sys.argv) - 1
i = 1 # counter variable

if arg < 1:
    print("{} arguments.".format(arg))
else:
    print("1 argument:" if arg == 1 else f"{arg} arguments:")
    while (i <= arg):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
