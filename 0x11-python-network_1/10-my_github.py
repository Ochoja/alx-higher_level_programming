#!/usr/bin/python3
"""Script that uses github API
to display id"""
import requests
import sys


user = sys.argv[1]
password = sys.argv[2]

try:
    req = requests.get('https://api.github.com/user', auth=(user, password))
    print(req.json()['id'])
except Exception:
    print(None)
