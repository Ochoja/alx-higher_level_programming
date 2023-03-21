#!/usr/bin/python3
"""Lists cities from the database hbtn_0e_4_usa
refer to './4-cities_by_state.sql' """
import sys
import MySQLdb


if __name__ == "__main__":
    # create connection to database
    db = MySQLdb.connect(host="localhost", user=f"{sys.argv[1]}",
                         password=f"{sys.argv[2]}", database=f"{sys.argv[3]}")

    # perform db query using cursor
    cursor = db.cursor()
    cursor.execute("SELECT ROW_NUMBER() OVER(ORDER BY cities.id), \
                    cities.name, states.name FROM states \
                    INNER JOIN cities ON states.id=cities.state_id")

    # get and print results
    result = cursor.fetchall()

    for i in result:
        print(i)

    # clean up
    cursor.close()
    db.close()
