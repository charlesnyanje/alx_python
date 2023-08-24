"""Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported."""

import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="Charles@26" db="hbtn_0e_0_usa")

cur = db.cursor()

cur.execute("USE hbtn_0e_0_usa")
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
for row in cur.fetchall():
    print(row)
