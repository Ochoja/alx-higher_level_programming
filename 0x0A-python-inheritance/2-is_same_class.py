#!/usr/bin/python3
"""
checks if objects belong to same class
"""


def is_same_class(obj, a_class):
    """
    check if `obj` belongs to `a_class`
    """
    if issubclass(obj, a_class):
        return True
    else:
        return False
