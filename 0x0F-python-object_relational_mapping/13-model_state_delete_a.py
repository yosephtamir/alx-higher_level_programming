#!/usr/bin/python3
"""This class is used to delate a word containing a"""
from sys import argv
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """This script runs"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State)

    for row in result:
        if 'a' in row.name:
            session.delete(row)
    session.commit()
