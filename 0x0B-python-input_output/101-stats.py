#!/usr/bin/python3
from sys import stdin

"""script that reads stdin line by line and computes metrics"""
status_code = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    402: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

totalsize = 0


def main():
    """Main function"""
    global status_code
    global totalsize
    linesCount = 0
    try:
        for line in stdin:
            splited = line.split()
            if len(splited) >= 2:
                code = splited[-2]
                totalsize += int(splited[-1])
                if code in status_code.keys():
                    status_code[code] += 1
            linesCount += 1

        if linesCount % 10 == 0:
            print_info()

        print_info()
    except KeyboardInterrupt:
        print_info()


def print_info():
    """Prints statics"""
    print(f"File size: {totalsize}")
    for key, value in sorted(status_code.items()):
        if value > 0:
            print("{:s}: {:d}".format(key, value))


if __name__ == "__main__":
    main()
