#!/usr/bin/python3
""" 8-rectangle: class Rectangle from BaseGeomerty"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializing  a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height