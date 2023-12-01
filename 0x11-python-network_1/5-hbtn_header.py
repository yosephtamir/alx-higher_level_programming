#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
import requests
from sys import argv


if __name__ == "__main__":
    """This script do not run if imported"""
    the_page = requests.get("{}".format(argv[1]))

    print(the_page.headers['X-Request-Id'])
