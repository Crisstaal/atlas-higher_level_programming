#!/usr/bin/python3
def print_last_digit(number):
    if number >=  0:
        lastdigit = number % -(10)
        print(-(last_digit), end= '')
    else:
        lastdigit = number % 10
        print(last_digit, end='')
    return abs(last_digit)
