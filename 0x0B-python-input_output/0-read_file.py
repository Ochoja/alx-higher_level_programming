#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """Reads a file"""
    with open(filename, encoding="UTF8") as text_file:
        print(text_file.read())

read_file("my_file_0.txt")
