import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:

    cursor = connection.cursor()

    cursor.execute("DROP TABLE if exists integers")
    cursor.execute("""CREATE TABLE integers(num INT)""")

    for i in range(100):
        cursor.execute('INSERT INTO integers VALUES(?)', (random.randint(0, 100),))
