"""Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported."""
import MySQLdb
import sys

def list_states_with_n_starting(username, password, database):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        
        # Create a cursor object to interact with the database
        cursor = db.cursor()
        
        # Execute the SQL query to retrieve states starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)
        
        # Fetch all the results
        results = cursor.fetchall()
        
        # Print the results
        for row in results:
            print(row)
        
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states_with_n_starting(username, password, database)
