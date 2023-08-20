#!/usr/bin/python3
"""
The script lists all states from the db hbtn_0e_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    This script only works directly
    """
    Mydb = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])

    Mycur = Mydb.cursor()
    Mycur.execute("SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %(state_name)s \
            ORDER BY cities.id ASC", {'state_name': argv[4]})
    rows = Mycur.fetchall()

    length = len(rows)
    for row in range(len(rows)):
        for colmn in rows[row]:
            if row < length - 1:
                print(colmn, end=", ")
            else:
                print(colmn)
