#!/usr/bin/python3

"""
1st state model
"""

from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """
        class which is a blueprint for State instances
        that links to  the MySQL table 'states'
    """
    __tablename__ = "states"
    id = Column('id', Integer(), primary_key=True)
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
