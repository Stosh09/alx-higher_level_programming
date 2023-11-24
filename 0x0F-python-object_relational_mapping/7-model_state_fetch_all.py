#!/usr/bin/python3

"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    states = session.query(State).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
