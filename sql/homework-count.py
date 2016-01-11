import sqlite3
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    models = ['A', 'B', 'C', 'D', 'E']

    for value in models:
        c.execute("SELECT * FROM inventory WHERE Model = ? ", (value))
        row = c.fetchone()
        print "Make:", row[0], "Model", row[1]
        print "quantity:", row[2]
        c.execute("SELECT count(model) FROM orders WHERE model = ? ", (value))
        print c.fetchone()[0]
