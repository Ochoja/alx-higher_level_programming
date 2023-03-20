#!/usr/bin/python3
"""Script connects to a database and prints data from a table"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Create connection to database
    db = MySQLdb.connect(host="localhost", user=f"{sys.argv[1]}",
                         password=f"{sys.argv[2]}", database=f"{sys.argv[3]}")

    # use cursor method to perform a db query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")

    # get results of query
    results = cursor.fetchall()

    for i in results:
        print(i)
