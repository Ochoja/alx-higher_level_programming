#!/usr/bin/python3
"""Script that sends request to URL and
displays the value of X-Request-Id"""
import urllib.request, sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        for x in str(response.info()).splitlines():
            if 'X-Request-Id' in x:
                request_id = x
        print(request_id.split()[1])
