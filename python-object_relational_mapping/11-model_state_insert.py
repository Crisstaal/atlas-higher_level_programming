#!/usr/bin/python3
"""Script that adds the State object "Louisiana" to the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]

    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    session = Session(engine)

    # Adding Louisiana to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print
    print(new_state.id)

    session.close()
