#!/usr/bin/python3

''' This is mysqldb module'''

import MySQLdb
from sys import argv


if __name__ == "__main__":

    '''
    This module lists all states in asc order
    '''
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    inp = argv[4]
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(query, (inp,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
