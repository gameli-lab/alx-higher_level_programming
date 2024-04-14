#!/usr/bin/python3

''' This is mysqldb module'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from model_state import Base, State
from model_city import City
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


    cities = (session.query(State.name, City.id, City.name)
              .select_from(State)
              .join(City, State.id == City.state_id)
              .order_by(City.id.asc())
              .all())


    for state_name, city_id, city_name in cities:
        print('{}: {}'.format(state_name, city_id, city_name))


    session.close()
