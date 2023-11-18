#!/usr/bin/python3
'''This script is used to filter a word with a'''
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    '''this only runs in the script'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    re = session.query(State).order_by(State.id).filter(State.name.like('%a%'))

    for instance in re:
        print("{}: {}".format(instance.id, instance.name))
