#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    List = sorted(a_dictionary.keys())
    for l in List:
        print("{:s}: {}".format(l, a_dictionary[l]))
