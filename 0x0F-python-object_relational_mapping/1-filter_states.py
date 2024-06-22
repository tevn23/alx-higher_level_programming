#!/usr/bin/python3
"""
Module containing function to list states
"""
import sys
import MySQLdb


def list_states_with_upper_N(username, password, database):
    """
    Lists all states with upper N from the database hbtn_0e_0_usa
    """
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
        query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)
        states = cursor.fetchall()

        if not states:
            sys.exit(0)
        
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        sys.exit(1)
    
    except Exception as e:
        sys.exit(1)
    
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states_with_upper_N(username, password, database)
