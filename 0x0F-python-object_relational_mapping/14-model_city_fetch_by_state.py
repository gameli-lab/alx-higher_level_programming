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

    cities = (session.query(States.name, Cities.id, Cities.name)
              .join(Cities).order_by(Cities.id.asc()).all())

'''select states.name, cities.id, cities.name from states 
join cities order by cities.id asc;'''

    for state_name, city_id, city_name in cities:
        print('{}: {}'.format(state.name, city.id, city.name))

    '''for i, state in enumerate(states, start=1):
        print('{}: {}'.format(i, state.name))'''

    session.close()
