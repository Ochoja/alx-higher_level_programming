#!/usr/bin/python3
from add_0 import add  # import add function

a = 1
b = 2

# prevent other modules from running this piece of code
# run only when this module is called by the interpreter
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
