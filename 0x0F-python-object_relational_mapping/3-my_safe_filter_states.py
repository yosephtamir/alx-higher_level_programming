#!/usr/bin/python3

"""
this is a safe filter
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """this runs"""
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %(nam)s \
                ORDER BY states.id ASC", {'nam': argv[4]})
    states = cur.fetchall()

    for rows in states:
        print(rows)
