#!/usr/bin/python3
""" defines a class square"""


class Square:
    """ defines a square"""
    def __init__(self, size=0):
        """ init square

        Args:
            value (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: value.

        Returns:
            nothing
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size.

        Args:
            value (int): size of the square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """return the area

        Returns:
            area.
        """
        return self.__size**2