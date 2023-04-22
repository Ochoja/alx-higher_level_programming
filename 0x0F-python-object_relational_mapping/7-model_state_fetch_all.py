#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
   with sqlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://argv[1]:argv[2]//@localhost/argv[3]')

    Base.metadata.create_all(engine)
    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
