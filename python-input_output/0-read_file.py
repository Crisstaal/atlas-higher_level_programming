#!/usr/bin/python3
""" Module defines a text file-reading function """


def read_file(filename=""):

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')