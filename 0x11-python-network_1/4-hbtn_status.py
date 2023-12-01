#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    """This script do not run if imported"""
    url = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(url) as response:
        the_page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page.decode("utf-8")))
