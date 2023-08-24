"""Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported."""

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user="", passwd=" ", port=3306, host="localhost")
    cur = db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa")
    cur.execute("USE hbtn_0e_0_usa")
    cur.execute("CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id))")
    cur.execute("INSERT INTO states (name) VALUES ('California'),('Arizona')")
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    
        