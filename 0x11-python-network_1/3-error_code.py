#!/usr/bin/python3
"""Script that send a request and decode the body in utf-8"""
from urllib.request import urlopen
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]  # holds url

    try:
        with urlopen(argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:  # handle HTTPError
        print(f"Error code: {e.code}")
