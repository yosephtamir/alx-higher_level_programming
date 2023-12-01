#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    """This script do not run if imported"""
    the_page = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(the_page.text)))
    print("\t- content: {}".format(the_page.text))
