#!/usr/bin/python3
"""
 a Python script that takes 2 arguments in order to solve this challenge.
"""
import requests
from sys import argv

if __name__ == "__main__":
    """This only runs in the script"""
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            argv[2], argv[1])
    resp = requests.get(url).json()
    count = 0

    for row in resp:
        count += 1
        print(row['sha'] + ':', row['commit']['author']['name'])
        if count > 9:
            break
