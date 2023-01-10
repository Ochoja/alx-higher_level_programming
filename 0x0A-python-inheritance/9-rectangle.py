#!/usr/bin/python3
"""
contains Rectangle class which inherits
from BaseGeometry
"""

BaseGeometry = __import__('8-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry
    """
    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
