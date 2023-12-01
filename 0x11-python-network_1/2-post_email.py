#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request to th
passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    """The code won't run if imported"""
    req = urllib.request.Request('{}'.format(argv[1]))
    val = {"email": "{}".format(argv[2])}
    data = urllib.parse.urlencode(val)
    data = data.encode("ascii")
    req = urllib.request.Request('{}'.format(argv[1]), data)

    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode("utf-8"))
