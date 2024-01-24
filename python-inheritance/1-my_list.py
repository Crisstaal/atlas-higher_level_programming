#!/usr/bin/python3
""" Module defines an inherited list class MyList."""


class MyList(list):

    def print_sorted(self):
        """Print list in ascending order."""
        print(sorted(self))