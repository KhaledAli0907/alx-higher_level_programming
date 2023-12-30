#!/usr/bin/python3
"""Module for student class"""


class Student:
    """Student class"""

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None) -> dict:
        """Retrives a dictionary representation of a student"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__

        result = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                result[key] = value
        return result
