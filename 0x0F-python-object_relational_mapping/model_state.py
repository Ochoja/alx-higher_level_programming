#!/usr/bin/python3
from sqlalchemy import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
