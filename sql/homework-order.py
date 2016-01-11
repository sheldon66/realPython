import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE orders(make TEXT, model TEXT, order_date TEXT)""")
    orders = [
            ('Ford', 'A', '2015-12-03'),('Ford', 'A', '2015-12-02'),('Ford', 'A', '2015-12-01'),
            ('Ford', 'B', '2015-12-05'),('Ford', 'B', '2015-12-07'),('Ford', 'B', '2015-12-09'),
            ('Ford', 'C', '2015-12-11'),('Ford', 'C', '2015-12-10'),('Ford', 'C', '2015-12-14'),
            ('Honda', 'D', '2015-12-20'),('Honda', 'D', '2015-12-17'),('Honda', 'D', '2015-12-18'),
            ('Honda', 'E', '2015-12-25'),('Honda', 'E', '2015-12-28'),('Honda', 'E', '2015-12-24'),
    ]
    c.executemany('INSERT INTO orders VALUES(?, ?, ?)', orders)
    c.execute("""SELECT inventory.Make, inventory.Model, inventory.quantity, orders.order_date FROM inventory, orders
                WHERE inventory.Model = orders.model""")

    rows = c.fetchall()

    for r in rows:
        print r
