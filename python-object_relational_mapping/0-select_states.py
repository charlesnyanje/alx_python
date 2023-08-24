"""Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported."""

import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="Charles@26")

cur = db.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa")
cur.execute("USE hbtn_0e_0_usa")
cur.execute("CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256), PRIMARY KEY (id))")
cur.execute("INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas'), ('Nevada'), ('Utah'), ('Colorado'), ('New Mexico'), ('Wyoming'), ('Montana'), ('Idaho'), ('Washington'), ('Oregon'), ('North Dakota'), ('South Dakota'), ('Nebraska'), ('Kansas'), ('Oklahoma'), ('Minnesota'), ('Iowa'), ('Missouri'), ('Arkansas'), ('Louisiana'), ('Wisconsin'), ('Illinois'), ('Mississippi'), ('Michigan'), ('Indiana'), ('Kentucky'), ('Tennessee'), ('Alabama'), ('Ohio'), ('West Virginia'), ('Virginia'), ('North Carolina'), ('South Carolina'), ('Georgia'), ('Florida'), ('Pennsylvania'), ('New York'), ('Vermont'), ('New Hampshire'), ('Maine'), ('Massachusetts'), ('Rhode Island'), ('Connecticut'), ('New Jersey'), ('Delaware'), ('Maryland'), ('Alaska'), ('Hawaii')")
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
for row in cur.fetchall():
    print(row)
cur.close()
db.close()