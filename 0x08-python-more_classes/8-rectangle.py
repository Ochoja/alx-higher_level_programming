#!/usr/bin/python3
"""Contains Rectangle class"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instantiation method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)

    def my_print(self):
        """
        method prints rectangle using '#'
        """
        if self.__width == 0 or self.__height == 0:
            pass
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("{}".format(self.print_symbol), end="")
                if i == self.__height - 1:
                    pass
                else:
                    print()

    def __str__(self):
        """
        runs when str() or print() is invoked
        with object as argument
        """
        self.my_print()
        return ""

    def __repr__(self):
        """
        runs when repr() is invoked with object
        as argument, also a fallback for __str__
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """runs when object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_2.area() > rect_1.area():
                return rect_2
            else:
                return rect_1
