#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """The code won't run if imported"""
    req = urllib.request.Request('{}'.format(argv[1]))

    with urllib.request.urlopen(req) as response:
        the_page = response.info()
        print(the_page["X-Request-Id"])
