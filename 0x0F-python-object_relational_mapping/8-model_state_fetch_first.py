#!/usr/bin/python3
"""List first state from db hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}
                           @localhost/{argv[3]}")

    Base.metadata.create_all(engine)  # connect model to db (create table)
    session = Session(engine)  # for CRUD operations


    for state in session.query(State).first():
        print(f"{state.id}: {state.name}")

    session.close()
