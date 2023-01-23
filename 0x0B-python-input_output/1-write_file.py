#!/usr/bin/python3
"""Writes to a file"""


def write_file(filename="", text=""):
    """writes a string to a file and returns
    the number of characters written"""
    with open(filename, mode='w', encoding="utf-8") as text_file:
        text_file.write(text)
        return len(text)
