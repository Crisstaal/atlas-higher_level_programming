#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        cursor = db.cursor()

        # Execute the SQL query to retrieve cities of the specified state
        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id;
        """
        cursor.execute(query, (state_name,))

        cities = cursor.fetchall()

        if cities:
            # Display the results
            city_names = ', '.join(city[0] for city in cities)
            print(city_names)
        else:
            print("No cities found for the specified state.")

    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close the database connection
        db.close()
