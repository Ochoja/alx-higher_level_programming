#!/usr/bin/python3
"""Script that sends request to URL and
displays the value of X-Request-Id"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = str(response.info()).splitlines()[16]
    print(x_request_id.split()[1])
