#!/usr/bin/python3
"""List information in a table using sqlalchemy"""
import sys
from model_state import Base, State  # contains table definition
from sqlalchemy import create_engine  # used to Connect to database
from sqlalchemy.orm import Session  # used for CRUD operations

url = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
print(url)
engine = create_engine(url, echo=True)

# Create table
Base.metadata.create_all(engine)  # Connect model to database engine
session = Session(engine)  # session is used for CRUD operations

for instance in session.query(State).order_by(State.id):
    print(f"{instance.id}: {instance.name}")

session.close()
