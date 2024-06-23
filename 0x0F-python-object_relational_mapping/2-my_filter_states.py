#!/usr/bin/python3
import sys
import MySQLdb

def main():
    # Ensure the script receives exactly 4 arguments (excluding the script name)
    if len(sys.argv) != 5:
        print("Usage: ./<script_name> <mysql_username> <mysql_password> <database_name> <state_name>")
        return

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Create a cursor object to interact with the database
        cur = db.cursor()

        # Execute the SQL query
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        # Fetch all the rows from the executed query
        rows = cur.fetchall()

        # Print the rows
        for row in rows:
            print(row)

        # Close the cursor and database connection
        cur.close()
        db.close()
    
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
        return

if __name__ == "__main__":
    main()
