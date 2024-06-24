#!/usr/bin/python3
"""
A script that takes in 3 safe arguments and lists all cities
from hbtn_0e_0_usa.

Usage:
./<script_name> <mysql_username> <mysql_password> <database_name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        c = db.cursor()
        query = ("SELECT cities.id, cities.name, states.name \
               FROM cities JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")
        c.execute(query)

        for result in c.fetchall():
            print(result)

    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        if c:
            c.close()
        if db:
            db.close()
