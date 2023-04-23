#!/usr/bin/python3
"""List first state from db hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    # create db connection
    url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(url)

    session = Session(engine)  # db handler

    state = session.query(State).first()

    print(f"{state.id}: {state.name}")
