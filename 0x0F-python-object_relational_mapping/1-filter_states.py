#!/usr/bin/python3
"""Lists all states with name starting with N"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Create connection to database
    db = MySQLdb.connect(host="localhost", user=f"{sys.argv[1]}",
                         password=f"{sys.argv[2]}", database=f"{sys.argv[3]}")

    # perform db query using cursor()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # query results
    results = cursor.fetchall()

    # Print results
    for i in results:
        print(i)
