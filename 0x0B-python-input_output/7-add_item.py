#!/usr/bin/python3
"""add all argument to a python list
and save them to a file"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
try:
    obj = load_from_json_file(filename)
    obj += sys.argv[1:]
    save_to_json_file(obj, filename)
except FileNotFoundError:
    with open(filename, mode='w') as json_file:
        obj = []
        obj += sys.argv[1:]
        save_to_json_file(obj, filename)
