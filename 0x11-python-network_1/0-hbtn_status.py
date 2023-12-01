#!/usr/bin/python3
import urllib.request
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    """The code won't run if imported"""
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')

    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("Body response:")
        print("    - type: {}".format(type(the_page)))
        print("    - content: {}".format(the_page))
        print("    - utf8 content: {}".format(the_page.decode("utf-8")))
