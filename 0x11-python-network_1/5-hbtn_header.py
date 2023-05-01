#!/usr/bin/python3
"""Sends a request and display the value of X-Request-Id"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
