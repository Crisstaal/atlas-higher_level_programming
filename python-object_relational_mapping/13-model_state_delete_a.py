#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection_string = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(connection_string.format(mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    # Query and delete all State objects with a name containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)

    session.commit()

    session.close()
