#!/usr/bin/python3
"""
script that lists all the states from the hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        exit()
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    result = cur.fetchall()
    for row in result:
        print(row)
