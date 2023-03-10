#!/usr/bin/python3
"""Function that executes a function safely"""
import sys


def safe_function(fct, *args):
    """Function executes fct safely"""
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
