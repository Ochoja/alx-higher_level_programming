#!/usr/bin/python3
"""Script fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {str(body)[2:len(str(body)) - 1]}")
