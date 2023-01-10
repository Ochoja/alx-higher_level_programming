#!/usr/bin/python3
"""
check if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    check if obj is an instance of a_class, or
    if obj is an instance of a class that inherited
    from a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
