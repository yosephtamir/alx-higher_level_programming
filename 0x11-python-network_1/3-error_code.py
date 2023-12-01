#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
"""
from sys import argv
from urllib import request
from urllib.error import HTTPError


if __name__ == "__main__":
    try:
        req = request.Request("{}".format(argv[1]))
        with request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode("utf-8"))
    except HTTPError as Err:
        print("Error code: {}".format(Err.code))
