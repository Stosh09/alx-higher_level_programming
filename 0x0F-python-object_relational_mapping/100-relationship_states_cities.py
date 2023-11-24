#!/usr/bin/python3

"""
    A script that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa:
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    new_state = State()
    new_state.name = "California"
    new_city = City()
    new_city.name = "San Francisco"
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()
