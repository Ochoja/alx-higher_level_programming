#!/usr/bin/python3
"""
contains BaseGeometry class
"""


class BaseGeometry:
    """
    class with one method which
    does nothing but raise an exception
    """
    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")
