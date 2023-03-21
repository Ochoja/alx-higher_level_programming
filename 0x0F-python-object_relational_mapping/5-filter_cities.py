#!/usr/bin/python3
"""
Takes in the name of a state as an argument
and lists all cities of that state refer to
'./4-cities_by_state.sql'
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # create connection to db
    db = MySQLdb.connect(host="localhost", user=f"{sys.argv[1]}",
                         password=f"{sys.argv[2]}", database=f"{sys.argv[3]}")

    # perform db query
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM cities WHERE state_id = \
                    (SELECT id FROM states WHERE name='{sys.argv[4]}')")

    # get and print results
    result = cursor.fetchall()

    index = 1
    for i in result:
        if index != len(result):
            print(i[2], end=", ")
        else:
            print(i[2])
        index += 1

    # clean up
    cursor.close()
    db.close()
