#!/usr/bin/python3

"""
Prints all City objects from the database hbtn_0e_14_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    rows = session.query(State.name, City.id, City.name)\
                  .select_from(City)\
                  .join((State, State.id == City.state_id))

    for row in rows:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
        