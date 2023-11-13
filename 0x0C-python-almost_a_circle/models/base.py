#!/usr/bin/python3
"""Base module file"""


import json


class Base:
    """Base clss for the project"""

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """initializing Class and assigning id to it"""
        if id != None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        # If list_dictionaries is None or empty, return "[]"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        # Otherwise, use the json module to convert the list of dictionaries to a JSON string
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        # Get the class name and use it as the filename
        filename = cls.__name__ + ".json"
        # Create an empty list to store the dictionaries of each object
        list_dicts = []
        # If list_objs is not None, loop through it and append the dictionary representation of each object to the list
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        # Use the static method to_json_string to convert the list of dictionaries to a JSON string
        json_string = cls.to_json_string(list_dicts)
        # Open the file in write mode and write the JSON string to it
        with open(filename, "w") as f:
            f.write(json_string)
