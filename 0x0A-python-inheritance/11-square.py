#!/usr/bin/python3
"""
Rectangle class that inherits from BaseGeometry
Square class that inherits from Rectangle
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


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """runs when print() or str() is called on instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("width", size)
        self.__size = size

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
