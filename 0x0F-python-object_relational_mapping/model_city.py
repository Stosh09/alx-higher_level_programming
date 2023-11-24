#!/usr/bin/python3

"""
    Another state model(city)
"""

from model_state import Base
from sqlalchemy import Integer, String, Column, ForeignKeyConstraint


class City(Base):
    """ class representing instance of Cities """
    __tablename__ = "cities"
    id = Column('id', Integer(), primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer(), nullable=False)
    ForeignKeyConstraint(['state_id'], ['states.id'])
