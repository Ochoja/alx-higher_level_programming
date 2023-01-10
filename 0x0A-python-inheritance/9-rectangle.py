#!/usr/bin/python3
"""
contains Rectangle class which inherits
from BaseGeometry
"""


class BaseGeometry:
    """
    Base geometry class

    """
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if not isinstance(name, str):
            raise TypeError("name must be a string")


"""Build a rectangle"""


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """str() method return"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
