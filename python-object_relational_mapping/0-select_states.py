#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # Extract MySQL credentials from command line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    
