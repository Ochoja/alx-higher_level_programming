#!/usr/bin/python3

# Print a string in uppercase
def uppercase(str):
    for char in str:
        print("{}".format(chr(ord(char) - 32)) if
              ord(char) < 123 and ord(char) > 96
              else f"{char}", end="")
    print("\n", end="")
