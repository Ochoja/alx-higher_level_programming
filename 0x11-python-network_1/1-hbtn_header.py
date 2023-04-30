#!/usr/bin/python3
"""Script that sends request to URL and
displays the value of X-Request-Id"""
import urllib.request, sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        for x in str(response.info()).splitlines():
            if 'X-Request-Id' in x:
                request_id = x
        print(request_id.split()[1])
