#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for i, a in new.items():
        new[i] = a*2
    return new