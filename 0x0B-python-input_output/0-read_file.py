#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """Reads a file"""
    with open(filename, encoding="UTF8", mode='r') as text_file:
        text_file.read()
