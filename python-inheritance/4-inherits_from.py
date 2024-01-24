#!/usr/bin/python3
""" 4-inherits_from: inherits_from() """


def inherits_from(obj, a_class):
    """
     Args:
            obj (object): object.
            a_class (class): class.
        Returns: True or False.
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
