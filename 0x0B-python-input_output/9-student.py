#!/usr/bin/python3
"""Module for student class"""


class Student:
    """Student class"""

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives a dictionary representation of a student"""
        return self.__dict__
