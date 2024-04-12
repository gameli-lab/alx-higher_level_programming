#!/usr/bin/python3
'''
MySQLdb module
'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    inp = argv[4]
    cur = db.cursor()

    query = "SELECT cities.name AS city_name FROM cities JOIN states ON cities.state_id=states.id WHERE states.name=%s ORDER BY cities.id ASC"

    cur.execute(query, (inp,))
    rows = cur.fetchall()

    city = ", ".join(row[0] for row in rows)
    print(city)
    cur.close()
    db.close()
