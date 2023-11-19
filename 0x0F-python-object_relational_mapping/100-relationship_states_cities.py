#!/usr/bin/python3
"""This class is used to list a city and state"""
from sys import argv
from sqlalchemy import create_engine
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
from relationship_city import City


if __name__ == "__main__":
    """This script runs"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
