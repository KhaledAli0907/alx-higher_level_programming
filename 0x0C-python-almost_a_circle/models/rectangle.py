# models/rectangle.py
"""Recatngle shape class based on base class"""
from models.base import Base


class Rectangle(Base):
    """A class that represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value  # Validate and assign value to the private attribute

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("heigth must be > 0")
        self.__height = value  # Validate and assign value to the private attribute

    @property
    def x(self):
        """Get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        self.__x = value  # Validate and assign value to the private attribute

    @property
    def y(self):
        """Get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        self.__y = value  # Validate and assign value to the private attribute

    def area(self) -> int:
        """calculate rectangle area"""
        return self.width * self.height

    def display(self) -> None:
        """Display rectangle cords to stdout"""
        for _ in range(0, self.height):
            for _ in range(0, self.width):
                print("#")
            print()

    def __str__(self) -> str:
        """String represintation to the class"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y}, - {self.width}/{self.height}"
        )
