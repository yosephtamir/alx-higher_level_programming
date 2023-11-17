#!/usr/bin/python3
"""
filtering by user input
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """
    This script runs if it is not imported
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
               ORDER BY states.id ASC".format(argv[4]))
    states = cur.fetchall()

    for rows in states:
        print(rows)
