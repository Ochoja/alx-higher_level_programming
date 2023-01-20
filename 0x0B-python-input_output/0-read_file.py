#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """Reads a file"""
    with open(filename, mode='r', encoding="utf-8") as text_file:
        print(text_file.readlines())
