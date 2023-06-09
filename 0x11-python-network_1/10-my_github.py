#!/usr/bin/python3
"""Script that uses github API
to display id"""
import requests
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    url = f'https://api.github.com/users/{user}'
    header = {'Authorization': f'token {password}'}

    try:
        req = requests.get(url, headers=header)
        print(req.json()['id'])
    except Exception:
        print(None)
