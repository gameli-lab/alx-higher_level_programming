#!/usr/bin/python3

''' This is mysqldb module'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''
    City inherits from Base
    '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer,ForeignKey('states.id'), nullable=False)
