#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, mode='r') as json_file:
        return json.load(json_file)
