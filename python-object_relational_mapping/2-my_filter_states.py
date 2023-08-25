"""Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys

def filter_statesby_input(username,password,database,search):
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            search=sys.argv[4]
        )
        
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(sys.argv[4]))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
        
if __name__ == "__main__":
    filter_statesby_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])