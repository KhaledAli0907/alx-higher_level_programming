#!/usr/bin/python3

"""Base module file"""


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
