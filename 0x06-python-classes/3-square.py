#!/usr/bin/python3
# 3-square.py
"""Defines a class Square with a private instance attribute size and a method to calculate its area."""


class Square:
    """Square class with a private size attribute and a method to calculate its area."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
