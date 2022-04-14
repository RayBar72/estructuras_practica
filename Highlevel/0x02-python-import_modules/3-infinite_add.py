#!/usr/bin/python3

def main():
    from sys import argv
    c = 0
    l = len(argv)
    for x in range(1, l):
        y = int(argv[x])
        c += y
    print("{}".format(c))

if __name__ == "__main__":
    main()