#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import the connect library from psycopg2
from psycopg2 import connect

table_name = "some_table"

# declare connection instance
conn = connect(
    dbname = "some_db",
    user = "objectrocket",
    host = "172.28.1.4",
    password = "1234"
)

# declare a cursor object from the connection
cursor = conn.cursor()

# execute an SQL statement using the psycopg2 cursor object
cursor.execute(f"SELECT * FROM {table_name};")

# enumerate() over the PostgreSQL records
for i, record in enumerate(cursor):
    print ("\n", type(record))
    print ( record )

# close the cursor object to avoid memory leaks
cursor.close()

# close the connection as well
conn.close()
