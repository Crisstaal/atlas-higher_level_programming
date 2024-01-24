#!/usr/bin/python3
"""Modules file-writing function."""


def write_file(filename="", text=""):
    """Writes a text file.

    Args:
        filename (str): name of the file.
        text (str): text to write
    Returns:
        Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
