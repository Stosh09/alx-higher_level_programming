#!/usr/bin/python3

"""
script that takes in the name of a state as an
argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name = %s ORDER BY cities.id", (argv[4],))

    for index, row in enumerate(cur.fetchall()):
        if index != 0:
            print(', ', end='')
        print(row[0], end='')
    print()
