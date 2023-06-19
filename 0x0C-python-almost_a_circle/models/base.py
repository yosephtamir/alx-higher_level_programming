#!/usr/bin/python3
"""
This is the base of all other class of this project
"""
from os import path
import json


class Base:
    """
    This is the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is an instantaniation
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This is used to read and return json strings
        """
        if list_dictionaries is None:
            return "[]"
        elif len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This is used to save a json file
        """
        newFile = cls.__name__ + '.json'
        jsonFile = []

        with open(newFile, 'w', encoding='utf-8') as file:
            if list_objs is None:
                return file.write(cls.to_json_string(None))

            for i in list_objs:
                jsonFile.append(i.to_dictionary())

            return file.write(cls.to_json_string(jsonFile))

    @staticmethod
    def from_json_string(json_string):
        """
        This is used to read from json string
        """
        if json_string is None:
            return []
        elif len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Updating the class method
        """
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Updating the class base
        """
        newFile = cls.__name__ + '.json'

        if path.exists(newFile) is False:
            return []

        with open(newFile, 'r', encoding='utf-8') as file:
            objs = cls.from_json_string(file.read())
            newInit = []

            for i in objs:
                newInit.append(cls.create(**i))

            return newInit
