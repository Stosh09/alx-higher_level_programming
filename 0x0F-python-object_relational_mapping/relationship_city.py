#!/usr/bin/python3

"""
    Another state model
"""

from relationship_state import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """ class representing instance of Cities """
    __tablename__ = "cities"
    id = Column('id', Integer(), primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
