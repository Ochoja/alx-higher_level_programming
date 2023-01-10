#!/usr/bin/python3
"""
checks if objects belong to same class
"""


def is_same_class(obj, a_class):
    """
    check if `obj` is an instance of `a_class`
    """
    # check if obj is a built in type
    if isinstance(obj, a_class) and a_class != object
        return True
    else:
        return False
