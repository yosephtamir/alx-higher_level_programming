#!/usr/bin/python3
"""Used to add a state into a database"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    """Entery point n"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    Louisiana = State("Louisiana")

    session.add(Louisiana)
    session.commit()

    print(Louisiana)
