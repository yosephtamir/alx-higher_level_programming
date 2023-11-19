#!/usr/bin/python3
"""This script is used to filter by arg passed"""
from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    """only runs if directly excuted"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State)
    flag = 0

    for nu in result:
        if nu.name == argv[4]:
            print(nu.id)
            flag = 1
            break
    if flag == 0:
        print("Not found")
