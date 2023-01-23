#!/usr/bin/python3
"""append string to end of file"""


def append_write(filename="", text=""):
    """append to a file or create one if file
    does not exist"""
    with open(filename, mode='a', encoding="utf-8") as text_file:
        text_file.write(text)
    return len(text)
