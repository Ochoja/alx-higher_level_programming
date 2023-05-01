#!/usr/bin/python3
"""Sends a request and display the value of X-Request-Id"""
import requests
from sys import argv

response = requests.get(argv[1])
print(response.headers['X-Request-Id'])