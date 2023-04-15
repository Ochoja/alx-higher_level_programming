#!/usr/bin/python3
from sqlalchemy import declarative_base
from sqlalchemy import Column, String, Integer, create_engine


Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
connection = engine.connect()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(), nullable=False)
