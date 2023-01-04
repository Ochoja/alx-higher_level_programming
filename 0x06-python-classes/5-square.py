#!/usr/bin/python3
"""
contains square class
"""


class Square:
    """class defines a square

    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """
        returns the area of the square

        """
        return self.__size ** 2

    @property
    def size(self):
        """size getter

        """
        return self.__size

    @size.setter
    def size(self, value):
        """size getter

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints the square with the character #

        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
