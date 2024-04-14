#!/usr/bin/python3

''' This is mysqldb module

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base = declarative_base()

    class States(Base):
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True, autoincrement=True,
                    nullable=False)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)

#!/usr/bin/python3
"""Start link class to table in database
"""'''
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
