#!/usr/bin/python3
"""
filter the cities name by the states name
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost', port=3306,
            charset='utf8', user=argv[1],
            passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
            "select cities.id, cities.name, states.name"
            " from cities join states on cities.state_id = states.id")
    query_rows = cur.fetchall()
    citieslist = ''
    for row in query_rows:
        if (row[2] == argv[4]):
            citieslist += row[1] + ', '
    if (len(citieslist) > 1):
        print(citieslist[:-2])
    cur.close()
    db.close()
