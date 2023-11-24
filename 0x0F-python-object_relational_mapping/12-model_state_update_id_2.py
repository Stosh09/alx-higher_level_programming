#!/usr/bin/python3

"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})
    session.commit()
