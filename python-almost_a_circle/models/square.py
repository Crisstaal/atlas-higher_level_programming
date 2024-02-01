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
            initialize square
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

    def to_dictionary(self):
        """
            Return the dictionary representation of a Square
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": seld.x,
            "y": self.y 
        }     
     def __str__(self):
        """
        Retrunn print representation
        """
        return "[Square] ({}) ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                             self.width)
