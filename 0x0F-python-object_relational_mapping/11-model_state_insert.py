#!/usr/bin/python3

"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    new_state = State()
    new_state.name = "Louisiana"

    session.add(new_state)
    session.commit()
    print(new_state.id)
