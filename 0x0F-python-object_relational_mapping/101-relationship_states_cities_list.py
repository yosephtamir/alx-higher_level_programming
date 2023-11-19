#!/usr/bin/python3
"""This class is used to list a city and state"""
from sys import argv
from sqlalchemy import create_engine
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base


if __name__ == "__main__":
    """This script runs"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id)

    for state in result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
