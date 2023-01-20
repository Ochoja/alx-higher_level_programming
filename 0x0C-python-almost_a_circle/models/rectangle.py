#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints rectangle"""
        for y_axis in range(self.__y):  # position on y-axis
            print()

        for i in range(self.__height):  # rows
            for x_axis in range(self.__x):  # position on x-axis
                print(" ", end="")
            for j in range(self.__width):  # columns
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update the Rectangle class"""
        if len(args) != 0:
            arg_list = [self.id, self.width, self.height, self.x, self.y]

            for i in range(len(args)):
                arg_list[i] = args[i]
            self.id, self.width, self.height, self.x, self.y = arg_list
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation of Rectangle
        Dictionary contains fields of class"""
        new_dict = {}
        for key, value in self.__dict__.items():
            new_dict[key.replace("_Rectangle__", "")] = value
        return new_dict

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"\
            f" - {self.__width}/{self.__height}"
