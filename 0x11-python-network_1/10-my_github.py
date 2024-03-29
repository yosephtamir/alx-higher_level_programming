#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    """This only runs in the script"""
    url = "https://api.github.com/user"
    resp = requests.get(url, auth=(argv[1], argv[2])).json()
    print(resp.get("id"))
