#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(argv[0]))
        exit(1)

    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    # Create an SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to find the State object with the given name
    result = session.query(State).filter(State.name == state_name).first()

    # print the result
    if result:
        print(result.id)
    else:
        print("Not found")
