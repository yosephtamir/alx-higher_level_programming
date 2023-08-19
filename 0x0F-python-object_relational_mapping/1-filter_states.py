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
    Mycur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                  ORDER BY states.id ASC")
    rows = Mycur.fetchall()

    for row in rows:
        print(row)
