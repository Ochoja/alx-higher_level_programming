#!/usr/bin/python3
"""student class"""


class Student():
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation of
        class instance"""
        return self.__dict__
