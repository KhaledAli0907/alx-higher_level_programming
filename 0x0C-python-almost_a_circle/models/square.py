#!/usr/bin/python3
"""
=======================
Module for Sqaure Class
=======================
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class to represent Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square"""
        # The size is equal to the width or height
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        # The size must be validated and assigned to both width and height
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs) -> None:
        """Update class"""
        # Update attributes with positional arguments
        if args and len(args) > 0:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        # Update attributes with keyword arguments
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self) -> dict:
        """Returns dictionary representation of a the Rectangle"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }
