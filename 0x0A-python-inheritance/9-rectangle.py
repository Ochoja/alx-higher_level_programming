#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry"""


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


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Constructor """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """ method that return de area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ string representation """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
