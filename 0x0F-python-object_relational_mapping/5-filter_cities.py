#!/usr/bin/python3
""" This is used to list a city associated to a state passed"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """This script runs if not imported"""

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities \
                     JOIN states ON cities.state_id = states.id \
                     WHERE states.name LIKE BINARY  %(ar)s \
                     ORDER BY cities.id ASC", {'ar': argv[4]})
    cities = cur.fetchall()

    if cities is not None:
        print(", ".join([row[1] for row in cities]))
