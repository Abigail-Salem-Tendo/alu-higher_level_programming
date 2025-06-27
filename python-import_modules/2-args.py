#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    print("{} argument{}{}".format(
        count,
        "" if count == 1 else "s",
        ":" if count else "."
    ))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
