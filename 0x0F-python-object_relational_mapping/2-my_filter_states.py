#!/usr/bin/python3
"""Module to run state table"""
import sys
import MySQLdb


def main():
    """Display state table values """
    if len(sys.argv) != 5:
        return

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

        cur = db.cursor()
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        db.close()

    except MySQLdb.Error:
        return


if __name__ == "__main__":
    main()
