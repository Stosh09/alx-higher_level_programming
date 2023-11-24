#!/usr/bin/python3

"""
State Model
"""

from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """
        class which is the blueprint for State instances
        that links to MySQL table 'states'
    """
    __tablename__ = "states"
    id = Column('id', Integer(), primary_key=True)
    name = Column('name', String(128), nullable=False)
