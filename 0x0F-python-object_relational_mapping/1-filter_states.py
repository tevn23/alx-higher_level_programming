#!/usr/bin/python3
"""
Module containing function to list states
"""
import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        if not username or not password or not database:
            sys.exit(1)

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = db.cursor()
        q = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(q)
        states = cursor.fetchall()

        if not states:
            sys.exit(0)

        for state in states:
            print(state)

    except Exception:
        sys.exit(1)

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
