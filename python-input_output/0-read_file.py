#!/usr/bin/python3
"""module defines a text file-reading function."""


def read_file(filename=""):
<<<<<<< HEAD

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
=======
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
>>>>>>> 9d5fdab78d1974c26e5cd9f4e39750ddcf9bf25a
