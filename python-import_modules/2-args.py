#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    if len(argv) == 1:
        print(f"{a - 1} arguments.")
    elif len(argv) == 2:
        print(f"{a - 1} argument:")
    else:
        print(f"{a - 1} arguments:")
    for argu in range(1, a):
        print(f"{argu}: {argv[argu]}")