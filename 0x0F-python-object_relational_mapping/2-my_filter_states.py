#!/usr/bin/python3
"""Takes argument and Display all values in
states table that matches argument"""
import sys
import MySQLdb


if __name__ == "__main__":
    # create connection to database
    db = MySQLdb.connect(host="localhost", user=f"{sys.argv[1]}",
                         password=f"{sys.argv[2]}", database=f"{sys.argv[3]}")

    # perform db query using cursor
    cursor = db.cursor()
    cursor.execute(f"""SELECT * FROM states WHERE
                   name={sys.argv[4]} ORDER BY id""")

    # get query result
    result = cursor.fetchall()

    # print result
    for i in result:
        print(i)
