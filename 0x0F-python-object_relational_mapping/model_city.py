#!/usr/bin/python3

''' This is mysqldb module'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sys import argv

Base = declarative_base()


class City(Base):
    '''
    States inherits from Base
    '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer,foreign_key=states.id, nullable=False)
