#!/usr/bin/python3
"""
Rectangle class that inherits from BaseGeometry
Square class that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle

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
