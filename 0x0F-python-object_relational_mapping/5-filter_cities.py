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

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as Mycur:
        Mycur.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })

        rows = Mycur.fetchall()
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
