#!/usr/bin/python3
"""Square inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class based on Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.width = value
        self.__size = value

    @property
    def height(self):
        return self.__size

    @height.setter
    def height(self, value):
        self.size = value
        self.height = value

    def update(self, *args, **kwargs):
        """updated arguments"""
        if len(args) > 0:
            arg_list = [self.id, self.size, self.x, self.y]
            for i in range(len(args)):
                arg_list[i] = args[i]
            self.id, self.size, self.x, self.y = arg_list
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
