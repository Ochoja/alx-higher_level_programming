#!/usr/bin/python3
"""Script that sends request to URL and
displays the value of X-Request-Id"""
import urllib.request
from sys import argv

url = argv[1]
req = urllib.request.Request(url)

if __name__ == "__main__":
    with urllib.request.urlopen(req) as response:
        for x in str(response.info()).splitlines():
            if 'X-Request-Id' in x:
                request_id = x
                break
        print(request_id.split()[1])
