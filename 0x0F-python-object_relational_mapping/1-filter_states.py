#!/usr/bin/python3

"""
This script is used to list a table starting from N
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """
    This is the main entery
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT *FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY states.id ASC")
    states = cur.fetchall()

    for rows in states:
        print(rows)
