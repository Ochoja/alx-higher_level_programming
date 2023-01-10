#!/usr/bin/python3
"""Square class that inherits from Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class which inherits from Rectangle"""
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area of square"""
        return self.__size ** 2

    def __str__(self):
        """string representation"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
