#!/usr/bin/python3
"""This acts as a base class for state"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from relationship_city import Base, City


class State(Base):
    """This is a state class used as a table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{}'.format(self.id)
