#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """This only runs in the script"""
    var = ''
    try:
        var = argv[1]
    except Exception:
        pass
    try:
        url = "http://0.0.0.0:5000/search_user"
        resp = requests.post(url, data={"q": var}).json()
        if var == '':
            print("No result")
        else:
            print("[{}] {}".format(resp["id"], resp["name"]))
    except Exception:
        print("Not a valid JSON")
