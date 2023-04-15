#!/usr/bin/python3
"""State model with sqlAlchemy"""
from sqlalchemy import declarative_base
from sqlalchemy.ext.declarative import Column, String, Integer


Base = declarative_base()

class State(Base):
    """Class creates the states table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
