#!/usr/bin/python3
"""List information in a table using sqlalchemy"""
import sys
from model_state import Base, State  # contains table definition


# Connect to database
from sqlalchemy import create_engine


url = f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
engine = create_engine(url, echo=True)

# Create table
Base.metadata.create_all(engine)  # Connect model to database engine


# Used for CRUD operations
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
for instance in session.query(states).order_by(states.id):
    print(f"{instance.id} {instance.name}")
