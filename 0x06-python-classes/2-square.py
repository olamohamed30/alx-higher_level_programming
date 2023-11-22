#!/usr/bin/python3
# 2-square.py
"""Defines a class Square with a private instance attribute size and validation."""

class Square:
    """Square class with a private size attribute and validation."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
