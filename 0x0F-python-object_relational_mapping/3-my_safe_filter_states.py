#!/usr/bin/python3

"""
script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument
This script should be safe from sql injections
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (argv[4],))

    for row in cur.fetchall():
        print(row)
