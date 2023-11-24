#!/usr/bin/python3

"""
script that lists all states from the database hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1], passwd=argv[2], database=argv[3])
    cur = database.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    for row in cur.fetchall():
        print(row)
