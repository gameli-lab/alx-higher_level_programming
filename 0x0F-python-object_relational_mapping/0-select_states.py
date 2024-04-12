#!/usr/bin/python3
import MYSQLdb


def list_states(username, password, database_name):

db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=databasename)

cursor = db.cursor()

query = "SELECT * FROM ststes ORDER BY states.id ASC"
cursor.execute(query)

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close
