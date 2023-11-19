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

    result = session.query(City).order_by(City.id)

    for city in result:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
