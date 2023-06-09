#!/usr/bin/python3
"""Script that uses github API
to display id"""
import requests
import sys


user = sys.argv[1]
password = sys.argv[2]
header = {'Authorization': f'token {password}'}

try:
    req = requests.get(f'https://api.github.com/users/{user}', headers=header)
    print(req.json()['id'])
except Exception:
    print(None)
