#!/usr/bin/python3

# check if character is lowercase
def islower(c):
    if ord(c) <= 122 and ord(c) >= 97:
        return True
    else:
        return False
