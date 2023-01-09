#!/usr/bin/python3
"""
Module contains add_integer function
add_integer:
Function adds two integers and returns the value
"""


def add_integer(a, b=98):
    """
    adds two integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = round(a)
    b = round(b)
    return a + b
