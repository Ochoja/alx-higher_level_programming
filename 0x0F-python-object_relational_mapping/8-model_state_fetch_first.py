#!/usr/bin/python3
"""List first state from db hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(url)

    Base.metadata.create_all(engine)  # connect model to db (create table)
    session = Session(engine)  # for CRUD operations

    count = 0
    for state in session.query(State).order_by(State.id).all():
        if count == 1:
            break
        print(f"{state.id}: {state.name}")
        count += 1

    session.close()
