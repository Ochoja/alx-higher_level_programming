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
        obj = []
        filename = cls.__name__ + ".json"

        if list_objs is not None:
            for instance in list_objs:
                obj.append(instance.to_dictionary())

        with open(filename, mode='w') as json_file:
            json_file.write(cls.to_json_string(obj))

    @staticmethod
    def from_json_string(json_string):
        """return the list of the JSON string representation"""
        if json_string == "" or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with attributes set
        using **dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(dictionary["width"], dictionary["height"])
        else:
            dummy = cls(dictionary["size"])

        dummy.update(**dictionary)
        return dummy
