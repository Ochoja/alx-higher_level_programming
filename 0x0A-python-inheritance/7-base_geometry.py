#!/usr/bin/python3
"""
contains BaseGeometry class
"""


class BaseGeometry:
    """
    Base geometry class
    """
    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if not isinstance(name, str):
            raise TypeError("name must be a string")
