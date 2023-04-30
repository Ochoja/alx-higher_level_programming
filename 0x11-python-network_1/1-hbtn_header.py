#!/usr/bin/python3
"""Script that sends request to URL and
displays the value of X-Request-Id"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
