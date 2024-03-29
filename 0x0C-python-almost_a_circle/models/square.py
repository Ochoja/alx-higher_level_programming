#!/usr/bin/python3
"""Square inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class based on Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
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

    def to_dictionary(self):
        """Returns dictionary of Square fields"""
        new_dict = super().to_dictionary()
        new_dict["size"] = new_dict["width"]
        del new_dict["width"], new_dict["height"]
        return new_dict
