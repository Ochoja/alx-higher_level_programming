#!/usr/bin/python3
"""converts an object to json
and write it to a file"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file"""
    with open(filename, mode='w') as text_file:
        json.dump(my_obj, text_file)
