#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    if (argc - 1) == 0:
        print("0 arguments.")
    elif (argc - 1) == 1:
        print("1 argument.")
    else:
        print(f"{argc} arguments.")
    for arg in range(1, argc):
        print(f"{arg}: {argv[arg]}")
