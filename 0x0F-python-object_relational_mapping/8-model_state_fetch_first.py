#!/usr/bin/python3
"""used to show a quiry"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print('{}: {}'.format(instance.id, instance.name))
