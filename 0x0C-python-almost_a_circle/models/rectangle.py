#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        def get_width(self):
            return self.__width

        def set_width(self, width):
            self.__width = width

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, height):
            return self.height

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, x):
            return self.x

        @property
        def y(self):
            return self.__y

        @y.setter
        def height(self, y):
            return self.y
