#!/usr/bin/python3
"""
defines a class rec
"""
class Rectangle:
    """Represents a rec withw ,h"""

    def __init__(self, width=0, height=0):
        """optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setsh of the rectanglenteger."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrif the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets ctangle, ensuring it's a valid integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

