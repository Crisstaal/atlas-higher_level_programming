#!/usr/bin/python3
""" Module defines a text file-reading function """


def read_file(filename=""):
      """ Function that reads from a file """

    with open(filename, 'r', encoding="utf-8") as f:
        print(read_data, end='')