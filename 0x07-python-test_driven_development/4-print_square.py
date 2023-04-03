#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """Print square depending on size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for row in range(size):
            print("#", end="")
        print("")
