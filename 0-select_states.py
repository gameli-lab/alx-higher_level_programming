#!/usr/bin/python3

''' This is mysqldb module'''

import MySQLdb


def list_states(username, password, database_name):

    '''
    This module lists all states in asc order
    '''
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
