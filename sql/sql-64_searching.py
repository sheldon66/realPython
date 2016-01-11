# SELECT statement
import sqlite3
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("SELECT firstname, lastname from employees")

    #fetchall() retrieves all records from the query
    rows = c.fetchall()

    #use a for loop to iterate through the database, printing the results line by line
    for r in rows:
        print r[0], r[1]
