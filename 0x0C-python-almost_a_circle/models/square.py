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
