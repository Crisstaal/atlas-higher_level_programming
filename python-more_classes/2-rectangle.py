#!/usr/bin/python3
"""
    2-rectangle: class Rectangle
"""


class Rectangle:
    """ class Rectangle """
    def __init__(self, width=0, height=0):
   """ Instantiation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
       if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height """
        if type(value) is not int:
        raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter of rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)
