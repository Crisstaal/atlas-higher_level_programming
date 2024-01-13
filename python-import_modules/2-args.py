#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    if len(argv) == 1:
        print(f"{a - 1} arguments.")
    elif len(argv) == 2:
        print(f"{a - 1} argument:")
    else:
<<<<<<< HEAD
        print(f"{a - 1} arguments:")
    for argu in range(1, a):
        print(f"{argu}: {argv[argu]}")
=======
        print("{:d} argument".format(len(sys.argv) - 1), end="")
        if len(sys.argv) > 2:
            print("s", end="")
        print(":")
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
>>>>>>> 50b29bf613ef19ae0ca8d85b1e4aea1580b43da3
