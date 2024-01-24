#!/usr/bin/python3
""" 3-is_kind_of_class: is_kind_of_class() """


def is_kind_of_class(obj, a_class):

    """Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If object is inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
