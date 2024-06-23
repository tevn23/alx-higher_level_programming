#!/usr/bin/python3
"""
A script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

Usage:
./<script_name> <mysql_username> <mysql_password> <database_name> <state_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        c = db.cursor()
        query = ("SELECT * FROM `states` WHERE BINARY `name` = '{}' "
                 "ORDER BY `id` ASC").format(state_name)
        c.execute(query)
        [print(state) for state in c.fetchall()]
    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        if c:
            c.close()
        if db:
            db.close()
