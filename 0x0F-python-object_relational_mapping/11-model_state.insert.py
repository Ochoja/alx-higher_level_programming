#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

# Create db connection
url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
engine = create_engine(url, echo=True)

# initiate db handler
session = Session(engine)

# add data to State table
new_state = State(name="Louisiana")
session.add(new_state)
session.commit()
