#!/usr/bin/python3
"""This script is used to list a merge of cites and state"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    '''the main entery'''
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")

    cities = cur.fetchall()

    for rows in cities:
        print(rows)
