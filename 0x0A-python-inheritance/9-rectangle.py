#!/usr/bin/python3
"""
contains Rectangle class which inherits
from BaseGeometry
"""

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
