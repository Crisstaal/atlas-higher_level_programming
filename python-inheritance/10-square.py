#!/usr/bin/python3
""" 10-square: Rectangle sub class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): size new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size