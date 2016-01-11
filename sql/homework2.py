import sqlite3
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [
            ('Ford', 'A', 1000),
            ('Ford', 'B', 2000),
            ('Ford', 'C', 1500),
            ('Honda', 'D', 1000),
            ('Honda', 'E', 1000)
    ]

    c.executemany('INSERT INTO  inventory VALUES(?, ?, ?)', cars)
