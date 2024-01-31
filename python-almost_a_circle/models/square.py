#!/usr/bin/python3
"""
    contains class Square implements class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Initialize a new square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initializes Square (overrides Rectangle init)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Set the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update square
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
            Overloading str function
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}