#!/usr/bin/python3
"""Script sends POST request"""
import requests
import sys


if __name__ == '__main__':
    if sys.argv[1]:
        arg = sys.argv[1]
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': arg})
    else:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q':""})

    response = r.json()
    
