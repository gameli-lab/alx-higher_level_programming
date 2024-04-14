#!/usr/bin/python3

''' This is mysqldb module'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":

    '''
    This module lists all states in asc order
    '''

    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.bind = engine
    dbs = sessionmaker(bind=engine)
    session = dbs()

    state = session.query(State).order_by(State.id.asc()).first()

    if state:
        print('{}: {}'.format(1, state.name))

    session.close()
