#!/usr/bin/python3
"""function that appends to a text file"""


def append_write(filename="", text=""):
    """ appends to a text file

    Args:
        filename: filename
        text: text to write

    Returns: number of characters

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)