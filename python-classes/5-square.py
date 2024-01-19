#!/usr/bin/python3
""" defines a class square"""


class Square:
    """ defines a square"""
    Attributes:
            size (int): size of square.

    def __init__(self, size=0):
        """ init square
            Args:
                size (int): size of the square.
        """
        self.__size = size
        
    @property
    def size(self):
        """int: size
        Returns:
        Private size.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """sets value of size
        Args:
            value (int): size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
    def area(self):
        """
             area of the square.
        """
        return self.__size * self.__size
    def my_print(self):
        """prints in output the square with the character #"""

        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()