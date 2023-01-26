#!/usr/bin/python3
"""
Contains Base class
"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string representation
        of its argument"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves list_objs to json file"""
        if list_objs is None:
            with open("Rectangle.json", mode='w') as filename:
                pass
        else:
            try:
                obj = []
                for instance in list_objs:
                    obj.append(instance.to_dictionary())
            except Exception as e:
                print(e, end=" ")
                print("Accepts Square or Rectangle instance only")
            else:
                if "size" in obj[0]:
                    with open("Square.json", mode='w') as filename:
                        filename.write(cls.to_json_string(obj))
                else:
                    with open("Rectangle.json", mode='w') as filename:
                        filename.write(cls.to_json_string(obj))
