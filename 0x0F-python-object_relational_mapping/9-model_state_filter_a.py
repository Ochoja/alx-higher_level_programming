#!/usr/bin/python3
"""Query all states which contain the letter `a` """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(url, echo=True)

    session = Session(engine)

    states = session.query(State).order_by(State.id).\
        filter(State.name.contains('a'))

    for state in states:
        print(f"{state.id}: {state.name}")
