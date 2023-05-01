#!/usr/bin/python3
"""Takes URL and email and sends POST request
to the passed URL with email as paramenter"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    response = requests.post(url, data={'email': email})

    print(response.text)
