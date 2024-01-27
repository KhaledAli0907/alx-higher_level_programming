#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    from urllib import request

    with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        cont = res.read()

        print(f'Body response:\n\
                \t- type: {type(cont)}\n\
                \t- content: {cont}\n\
                \t -utf8 content: {cont.decode("utf-8")}')
