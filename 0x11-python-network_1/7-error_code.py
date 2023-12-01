#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the body of the response.
"""
from sys import argv
import requests


if __name__ == "__main__":
    """This runs only directly"""
    resp = requests.get("{}".format(argv[1]))
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
