#!/usr/bin/python3
"""
script that lists all the states from the hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 5):
        exit()
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    arg = sys.argv[4]
    cur.execute("SELECT * from states where name='{}' order by id".format(arg))
    result = cur.fetchall()
    for row in result:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()
