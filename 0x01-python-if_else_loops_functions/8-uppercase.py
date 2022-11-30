#!/usr/bin/python3

# Print a string in uppercase
def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("\n" if char == str[len(str) - 1] else "f{char}", end="")
