#!/usr/bin/python3
"""This class is used to list a city and state"""
from sys import argv
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    """This script runs"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).filter(City.state_id == State.id) \
                    .order_by(City.id)
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
