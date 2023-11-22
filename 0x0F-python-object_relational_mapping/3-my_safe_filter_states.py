#!/usr/bin/python3
"""
displays all values in a safe way
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    if (len(argv) != 5):
        exit()
    db = MySQLdb.connect(
            host="localhost", port=3306,
            charset="utf8", user=argv[1],
            passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s order by id", (argv[4],))
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()
