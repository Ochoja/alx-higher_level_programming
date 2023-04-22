#!/usr/bin/python3
"""Takes argument and Display all values in
states table that matches argument"""
import sys
import MySQLdb


if __name__ == "__main__":
    # create connection to database
    db = MySQLdb.connect(host="localhost", port=3306, user=f"{sys.argv[1]}",
                         password=f"{sys.argv[2]}", database=f"{sys.argv[3]}")

    # perform db query using cursor
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE \
                   name='{}' ORDER BY id".format(sys.argv[4]))

    # get query result
    result = cursor.fetchall()

    # print result
    for i in result:
        print(i)

    # clean up (close cursor/db)
    cursor.close()
    db.close()
