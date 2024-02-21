#!/usr/bin/python3
import MySQLdb
import sys

def list_cities_by_state(username, password, database):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    # Execute the SQL query
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities_by_state(username, password, database)
