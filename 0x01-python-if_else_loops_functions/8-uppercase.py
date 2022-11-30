#!/usr/bin/python3

# Print a string in uppercase
def uppercase(str):
    for character in str:
        if ord(character) > 96 and ord(character) < 123:
            print("{}".format(chr(ord(character) - 32), end="")
        else:
            print(f"{character}")
