#!/usr/bin/python3

''' This is mysqldb module'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base = declarative_base()

    class States(Base):
        '''
        States inherits from Base
        '''
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True, autoincrement=True,
                    nullable=False)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
