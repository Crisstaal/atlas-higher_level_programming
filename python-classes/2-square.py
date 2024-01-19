#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    """defines a square
    Attributes:
        __size (int): size of side
    """
    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of a side
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size