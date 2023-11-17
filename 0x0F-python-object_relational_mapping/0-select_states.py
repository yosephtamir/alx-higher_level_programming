#!/usr/bin/python3
"""
This script is used to list all the files in hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """
    this runs directly
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()

    for rows in states:
        print(rows)
