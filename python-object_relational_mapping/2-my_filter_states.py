"""Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb

def filter_statesby_input(username,password,database,search):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(search))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()