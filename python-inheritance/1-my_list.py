#!/usr/bin/python3
"""1-my_list: class MyList"""


class MyList(list):
    """
        class inherits from list.
        Methods:
            print_sorted - prints the list in ascending order
    """
    def print_sorted(self):
        """
           prints list in ascending order.
        """
        print(sorted(self))